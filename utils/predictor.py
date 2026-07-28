import joblib
import pandas as pd


model = joblib.load("student_model.pkl")


def performance_level(score):

    if score >= 85:
        return "Excellent"

    elif score >= 70:
        return "Good"

    elif score >= 50:
        return "Average"

    return "Poor"


def recommend_career(
    math,
    science,
    english,
    computer
):

    if computer >= 90:
        return "AI Engineer"

    elif math >= 85:
        return "Software Engineer"

    elif science >= 85:
        return "Doctor"

    elif english >= 85:
        return "Teacher"

    return "Business Analyst"


def predict_performance(
    study_hours,
    attendance,
    math_marks,
    science_marks,
    english_marks,
    computer_marks
):

    try:

        input_data = pd.DataFrame([{
            "study_hours": study_hours,
            "attendance": attendance,
            "math": math_marks,
            "science": science_marks,
            "english": english_marks,
            "computer": computer_marks
        }])

        score = float(model.predict(input_data)[0])

        score = max(0, min(score, 100))

        subjects = {
            "Math": math_marks,
            "Science": science_marks,
            "English": english_marks,
            "Computer": computer_marks
        }

        weak_subject = min(
            subjects,
            key=subjects.get
        )

        strong_subject = max(
            subjects,
            key=subjects.get
        )

        return {
            "score": round(score, 2),
            "level": performance_level(score),
            "weak_subject": weak_subject,
            "strong_subject": strong_subject,
            "career": recommend_career(
                math_marks,
                science_marks,
                english_marks,
                computer_marks
            )
        }

    except Exception as e:

        return {
            "score": 0,
            "level": "Error",
            "weak_subject": "N/A",
            "strong_subject": "N/A",
            "career": "N/A",
            "error": str(e)
        }