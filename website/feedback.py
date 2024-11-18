from flask import Flask, render_template, request
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)

# Load the fine-tuned model and tokenizer
model = GPT2LMHeadModel.from_pretrained("./models/fine_tuned_model")  # Path to your fine-tuned model
tokenizer = GPT2Tokenizer.from_pretrained("./models/fine_tuned_model")

# Function to generate feedback using the fine-tuned model
def generate_feedback(user_input):
    inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True, max_length=512)
    outputs = model.generate(inputs["input_ids"], max_length=150, num_return_sequences=1, temperature=0.7, top_p=0.9, top_k=50)
    feedback = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return feedback

@app.route('/')
def index():
    return render_template('behavioral.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    # Debug: Check if the form data is received correctly
    user_input = request.form.get('answer')
    
    if not user_input:
        print("No answer received!")  # Debugging: Check if the input is empty
    else:
        print("User answer:", user_input)  # Debugging: Print the user's input
    
    # Generate feedback
    feedback = generate_feedback(user_input)
    
    # Return the feedback and answer to the user and render it in feedback.html
    return render_template('feedback.html', answer=user_input, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
