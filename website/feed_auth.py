from flask import Flask, request, render_template
from feedback import generate_feedback

app = Flask(__name__)

@app.route('/submit_interview_answer', methods=['POST'])
def submit_interview_answer():
    if request.method == 'POST':
        user_answer = request.form.get('answer')  # The user's answer from a form
        feedback = generate_feedback(user_answer)
        
        # Render the feedback on a page
        return render_template('feedback.html', feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)
