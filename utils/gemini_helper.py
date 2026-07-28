import google.generativeai as genai
from config import Config


# =====================================================
# GEMINI API CONFIGURATION
# =====================================================

genai.configure(
    api_key=Config.GEMINI_API_KEY
)

# Latest Stable Model
model = genai.GenerativeModel(
    "gemini-flash-latest"
)


# =====================================================
# AI FEEDBACK GENERATOR
# =====================================================

def generate_ai_feedback(student_data):

    try:

        prompt = f"""

You are an Advanced Educational AI Assistant.

Your job is to analyze a student's academic performance professionally.


IMPORTANT RULES:

1. Keep the response between 80 to 150 words.
2. Use simple and professional English.
3. Keep the response student friendly.
4. Use concise and pointwise explanations.
5. Never generate unnecessarily large answers.
6. Stay focused only on student performance.
7. Never repeat the same information.


Generate ONLY the following sections:


Performance Analysis:
.....


Performance Level:
.....


Strong Subject:
.....


Weak Subject:
.....


Improvement Suggestions:
• ....
• ....
• ....


Daily Study Plan:
• ....
• ....
• ....


Career Guidance:
• ....
• ....


Recommended Technologies:
• ....
• ....


Project Suggestions:
• ....
• ....


Motivation:
.....




Student Details:


Study Hours:
{student_data['study_hours']}


Attendance:
{student_data['attendance']}


Math Marks:
{student_data['math']}


Science Marks:
{student_data['science']}


English Marks:
{student_data['english']}


Computer Marks:
{student_data['computer']}



IMPORTANT:

Always keep responses:

• Professional
• Accurate
• Precise
• Student Friendly
• Pointwise
• Easy to Understand

"""

        print("\n========== AI FEEDBACK CALLED ==========\n")

        response = model.generate_content(
            prompt
        )

        print("\n========== AI FEEDBACK SUCCESS ==========\n")

        return response.text

    except Exception as e:

        print("\n========== AI FEEDBACK ERROR ==========\n")

        print(e)

        print("\n=========================================\n")

        return """

Performance Analysis:

Your academic performance is satisfactory.



Improvement Suggestions:

• Study regularly.

• Improve your attendance.

• Practice weak subjects daily.

• Maintain consistency in learning.



Daily Study Plan:

• Study for 3-4 hours daily.

• Revise important topics regularly.

• Practice problem solving daily.



Career Guidance:

• Continue improving your technical skills.

• Focus on your academic goals.



Motivation:

Stay consistent and believe in yourself.
Success comes through continuous learning.

"""



# =====================================================
# CHATBOT
# =====================================================

def chatbot_response(message):

    msg = message.lower().strip()


    # =================================================
    # GREETINGS
    # =================================================

    greetings = [

        "hi",
        "hii",
        "hiii",
        "hello",
        "hey",
        "heyy",
        "hola",
        "good morning",
        "good afternoon",
        "good evening"

    ]


    if any(word in msg for word in greetings):

        return """

Hello!

I'm your Educational AI Assistant.


I can help you with:

• Programming

• Artificial Intelligence

• Machine Learning

• Career Guidance

• Computer Science

• Academic Subjects

• Interview Preparation

• Student Performance Analysis



How can I help you today?

"""


    elif "thank" in msg:

        return """

You're welcome!

Happy Learning.

"""


    elif "bye" in msg:

        return """

Goodbye!

Keep learning and have a wonderful day.

"""


    # =================================================
    # GEMINI AI RESPONSE
    # =================================================

    try:

        prompt = f"""

You are an Advanced Educational AI Assistant.


==================================================

IMPORTANT RULES

==================================================


1. Always provide accurate and precise answers.


2. Use simple and professional English.


3. Default response length must be between
100 to 200 words.


4. Never exceed 300 words unless explicitly
requested by the user.


5. Never generate unnecessarily large answers.


6. Always prefer pointwise explanations.


7. Keep responses visually clean.


8. Never repeat the same information.


9. Never assume information that the user
has not provided.


10. Stay focused only on the user's question.


11. Never mention that you are an AI model
unless explicitly asked.


12. Avoid unnecessary paragraphs.


13. Use bullet points whenever possible.


14. If the answer can be given briefly,
never increase the response length.


15. Always use student friendly explanations.


==================================================

FOR NORMAL QUESTIONS

==================================================


Provide:


Definition:
......


Key Points:

• ......

• ......

• ......



Example:
......



Applications:

• ......

• ......



Conclusion:
......



==================================================

FOR TECHNICAL QUESTIONS

==================================================


Provide:


Definition:
......


Key Concepts:
......


Example:
......


Applications:
......


Conclusion:
......



==================================================

FOR PROGRAMMING QUESTIONS

==================================================


Provide:


Definition:
......


Code Example:
......


Expected Output:
......


Explanation:
......


Time Complexity:
(if required)


Space Complexity:
(if required)


Applications:
......


Best Practices:
......



==================================================

FOR CAREER GUIDANCE

==================================================


Provide:


• Required Skills

• Career Roadmap

• Recommended Technologies

• Project Suggestions

• Study Tips

• Interview Preparation Tips

• Career Opportunities

• Learning Resources



==================================================

FOR INTERVIEW PREPARATION

==================================================


Provide:


• Important Questions

• Answers

• Preparation Tips

• Important Topics

• Best Practices

• Learning Resources



==================================================

FOR STUDENT GUIDANCE

==================================================


Provide:


• Study Tips

• Learning Strategies

• Improvement Suggestions

• Daily Study Plan

• Weekly Study Plan

• Motivation



==================================================

ONLY WRITE LONG ANSWERS IF THE USER ASKS

==================================================


Examples:


• Explain in detail.

• Explain deeply.

• Write 500 words.

• Write an essay.

• Write a report.

• Write a paragraph.

• Describe completely.



==================================================

DETAILED MODE

==================================================


Response Length:

300 to 500 words.



==================================================

ESSAY / REPORT MODE

==================================================


Response Length:

500+ words.



==================================================

IMPORTANT FORMATTING RULES

==================================================


1. Never use:

#

##

###


unless explicitly requested.



2. Never use fancy symbols or decorations.



3. Keep responses suitable for:

• School Students
• College Students
• B.Tech Students
• Interview Preparation
• Academic Learning



4. Always keep answers:

• Professional
• Accurate
• Precise
• Pointwise
• Student Friendly
• Easy to Understand
• Visually Clean



5. For simple questions provide simple answers.


6. For technical questions provide structured answers.


7. For programming questions provide code and explanations.


8. If the user asks follow-up questions like:

• Explain More
• Continue
• Give Example
• Explain Deeply

Provide a more detailed explanation while
remaining focused on the user's topic.



==================================================

USER QUESTION

==================================================


{message}



==================================================

FINAL INSTRUCTIONS

==================================================


Always provide:

• Professional Responses

• Educational Guidance

• Accurate Information

• Concise Explanations

• Student Friendly Language

• Production Quality Outputs


"""

        print("\n========== CHATBOT API CALLED ==========\n")

        response = model.generate_content(
            prompt
        )

        print("\n========== CHATBOT RESPONSE RECEIVED ==========\n")

        return response.text

    except Exception as e:

        print("\n========== CHATBOT ERROR ==========\n")

        print(e)

        print("\n==============================================\n")

        return """

Sorry!

The AI Assistant is currently unavailable.

Please try again after some time.



You can still use the following features:

• Student Performance Prediction

• Academic Guidance

• Career Guidance

• Programming Support

• Machine Learning Concepts

• Artificial Intelligence Concepts

• Computer Science Subjects

• Interview Preparation

• Student Performance Analysis



Thank You.

"""