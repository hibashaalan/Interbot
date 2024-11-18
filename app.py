from flask import Flask, render_template, request, jsonify
import subprocess
import os
import sys
from feedback import check_feedback
import requests
from flask import Flask, jsonify


app = Flask(__name__)
### new get questions function 
@app.route('/get_questions', methods=['GET'])
def get_questions():
    questions = []
    
    # Read questions from the questions.txt file
    try:
        with open('questions.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    slug, title = line.split(':', 1)  # Split by colon
                    questions.append({"titleSlug": slug.strip(), "title": title.strip()})
    except FileNotFoundError:
        return jsonify({"error": "Questions file not found"}), 500

    # Return questions from the file
    return jsonify(questions)

@app.route('/get_question_details', methods=['GET'])
def get_question_details():
    slug = request.args.get('slug')
    if not slug:
        return jsonify({"error": "No slug provided"}), 400

    url = "https://leetcode.com/graphql"
    query = {
        "query": f"""
        query {{
            question(titleSlug: "{slug}") {{
                content
            }}
        }}
        """
    }

    response = requests.post(url, json=query)
    if response.status_code == 200:
        question_data = response.json()
        question_content = question_data['data']['question']['content']
        return jsonify({"content": question_content})
    else:
        return jsonify({"error": "Failed to fetch question details"}), 500


@app.route('/')
def editor():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data.get('code', '')
    
    # Write the code to a temporary file
    temp_file = 'temp_script.py'
    with open(temp_file, 'w') as f:
        f.write(code)

    # Use subprocess to run the code and capture output
    try:
        # Run the script and capture output
        output = subprocess.check_output([sys.executable, temp_file], stderr=subprocess.STDOUT, text=True)
        result = {'output': output}
    except subprocess.CalledProcessError as e:
        result = {'error': e.output}
    except Exception as e:
        result = {'error': f"Unexpected error: {str(e)}"}
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_file):
            os.remove(temp_file)

    return jsonify(result)

@app.route('/feedback', methods=['POST'])
def get_feedback():
    data = request.get_json()
    user_output = data.get("user_output")
    question_index = data.get("question_index", 0)  # Default to first question if no index is provided

    # Get expected output from the dataset
    expected_output = greengerong_train[question_index]["answer"]  # Make sure this field exists in your dataset

    # Provide feedback using the imported check_feedback function
    feedback = check_feedback(user_output, expected_output)
    return jsonify({"feedback": feedback})

if __name__ == "__main__":
    app.run(debug=True)
