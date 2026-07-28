from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(filename, student_data, prediction_data, ai_feedback):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "AI Student Predictor Report",
            styles['Title']
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            f"Study Hours: {student_data['study_hours']}",
            styles['Normal']
        )
    )

    elements.append(
        Paragraph(
            f"Attendance: {student_data['attendance']}",
            styles['Normal']
        )
    )

    elements.append(
        Paragraph(
            f"Math: {student_data['math']}",
            styles['Normal']
        )
    )

    elements.append(
        Paragraph(
            f"Science: {student_data['science']}",
            styles['Normal']
        )
    )

    elements.append(
        Paragraph(
            f"English: {student_data['english']}",
            styles['Normal']
        )
    )

    elements.append(
        Paragraph(
            f"Computer: {student_data['computer']}",
            styles['Normal']
        )
    )

    elements.append(Spacer(1, 15))

    elements.append(
        Paragraph(
            f"Performance Score: {prediction_data['score']}",
            styles['Normal']
        )
    )

    elements.append(
        Paragraph(
            f"Level: {prediction_data['level']}",
            styles['Normal']
        )
    )

    elements.append(
        Paragraph(
            f"Career: {prediction_data['career']}",
            styles['Normal']
        )
    )

    elements.append(
        Paragraph(
            f"Strong Subject: {prediction_data['strong_subject']}",
            styles['Normal']
        )
    )

    elements.append(
        Paragraph(
            f"Weak Subject: {prediction_data['weak_subject']}",
            styles['Normal']
        )
    )

    elements.append(Spacer(1, 15))

    elements.append(
        Paragraph(
            "AI Feedback",
            styles['Heading2']
        )
    )

    elements.append(
        Paragraph(
            ai_feedback,
            styles['Normal']
        )
    )

    doc.build(elements)

    return filename