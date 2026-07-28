from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import send_file
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user
)

from werkzeug.security import generate_password_hash, check_password_hash

from config import Config

from utils.predictor import predict_performance
from utils.gemini_helper import generate_ai_feedback
from utils.gemini_helper import chatbot_response
from utils.pdf_generator import generate_pdf


app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

login_manager = LoginManager()

login_manager.init_app(app)


# DATABASE MODELS


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100))

    email = db.Column(db.String(100), unique=True)

    password = db.Column(db.String(200))

    xp = db.Column(db.Integer, default=0)

    streak = db.Column(db.Integer, default=0)

class Prediction(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)

    study_hours = db.Column(db.Float)

    attendance = db.Column(db.Float)

    math_marks = db.Column(db.Float)

    science_marks = db.Column(db.Float)

    english_marks = db.Column(db.Float)

    computer_marks = db.Column(db.Float)

    performance_score = db.Column(db.Float)

    performance_level = db.Column(db.String(100))

    weak_subject = db.Column(db.String(100))

    strong_subject = db.Column(db.String(100))

    career = db.Column(db.String(100))

    ai_feedback = db.Column(db.Text)


# LOGIN MANAGER


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


# HOME


@app.route('/')
def index():

    return render_template('index.html')


# REGISTER


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']

        email = request.form['email']

        password = generate_password_hash(
            request.form['password']
        )

        user = User(
            username=username,
            email=email,
            password=password
        )

        db.session.add(user)

        db.session.commit()

        return redirect('/login')

    return render_template('register.html')


# LOGIN


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']

        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(
            user.password,
            password
        ):

            login_user(user)

            return redirect('/dashboard')

    return render_template('login.html')


# LOGOUT


@app.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect('/')


# DASHBOARD


@app.route('/dashboard')
@login_required
def dashboard():

    predictions = Prediction.query.filter_by(
        user_id=current_user.id
    ).all()

    total_predictions = len(predictions)

    if total_predictions > 0:
        avg_score = sum(
            [p.performance_score or 0
             for p in predictions]
        ) / total_predictions
    else:
        avg_score = 0

    if predictions:
        latest = predictions[-1]
    else:
        latest = None

    return render_template(
        'dashboard.html',
        predictions=predictions,
        total_predictions=total_predictions,
        avg_score=avg_score,
        latest=latest
    )


# PREDICTOR


@app.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():

    if request.method == 'POST':

        study_hours = float(
            request.form['study_hours']
        )

        attendance = float(
            request.form['attendance']
        )

        math_marks = float(
            request.form['math_marks']
        )

        science_marks = float(
            request.form['science_marks']
        )

        english_marks = float(
            request.form['english_marks']
        )

        computer_marks = float(
            request.form['computer_marks']
        )

        result = predict_performance(
            study_hours,
            attendance,
            math_marks,
            science_marks,
            english_marks,
            computer_marks
        )

        ai_feedback = generate_ai_feedback({
            'study_hours': study_hours,
            'attendance': attendance,
            'math': math_marks,
            'science': science_marks,
            'english': english_marks,
            'computer': computer_marks
        })

        prediction = Prediction(
            user_id=current_user.id,
            study_hours=study_hours,
            attendance=attendance,
            math_marks=math_marks,
            science_marks=science_marks,
            english_marks=english_marks,
            computer_marks=computer_marks,
            performance_score=result['score'],
            performance_level=result['level'],
            weak_subject=result['weak_subject'],
            strong_subject=result['strong_subject'],
            career=result['career'],
            ai_feedback=ai_feedback
        )
        current_user.xp += 10
        current_user.streak += 1
        
        db.session.add(prediction)
        db.session.add(current_user)

        db.session.commit()

        return render_template(
            'report.html',
            result=result,
            feedback=ai_feedback
        )

    return render_template('predictor.html')


#HISTORY


@app.route('/history')
@login_required
def history():

    predictions = Prediction.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        'history.html',
        predictions=predictions
    )

@app.route('/admin')
@login_required
def admin():

    users = User.query.all()

    predictions = Prediction.query.all()

    return render_template(
        'admin.html',
        users=users,
        predictions=predictions
    )
@app.route('/download-report/<int:id>')
@login_required
def download_report(id):

    prediction = Prediction.query.get_or_404(id)

    student_data = {
        "study_hours": prediction.study_hours,
        "attendance": prediction.attendance,
        "math": prediction.math_marks,
        "science": prediction.science_marks,
        "english": prediction.english_marks,
        "computer": prediction.computer_marks
    }

    prediction_data = {
        "score": prediction.performance_score,
        "level": prediction.performance_level,
        "career": prediction.career,
        "strong_subject": prediction.strong_subject,
        "weak_subject": prediction.weak_subject
    }

    filename = f"report_{prediction.id}.pdf"

    generate_pdf(
        filename,
        student_data,
        prediction_data,
        prediction.ai_feedback
    )

    return send_file(
        filename,
        as_attachment=True
    )


# CHATBOT


@app.route('/chatbot')
@login_required
def chatbot():

    return render_template('chatbot.html')

@app.route('/chat-api', methods=['POST'])
@login_required
def chat_api():

    data = request.get_json()

    message = data.get('message')

    response = chatbot_response(message)

    return jsonify({
        "response": response
    })


# RUN


if __name__ == '__main__':

    with app.app_context():

        db.create_all()

    app.run(debug=True)