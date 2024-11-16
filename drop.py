from flask import Flask
from flask import Blueprint, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"]='ai_dropdown'

@app.route('/technical', methods=['GET', 'Post'])
def technical():
    return render_template('technical.html')

#create route for role selection

#Roles selection
def RoleSelection():

    role = [('Software Engineer', 'Machine Learning', 'AI Engineer', 'Data Analyst', 'Full Stack Developer', 'Game Designer', 'Web Developer', 'Cybersecurity', 'DevOper', 'Product Management')]
    if request.method == 'POST':
        selected_option == request.form['role_choice']
        return "You selected: {selected_option}"
    return render_template('technical.html')

#Select what company they want
@app.route('/company')
def technical():
    return render_template('company.html')

def CompanySelection():

    role = [('Google', 'Amazon', 'Microsoft', 'Facebook', 'Apple', 'Netflix', 'LinkedIn', 'Salesforce', 'Airbnb', 'Stripe')]
    if request.method == 'POST':
        selected_option == request.form['company_choice']
        return "You selected: {selected_option}"
    return render_template('company.html')

if __name__ == '__main__':
    app.run(debug=True)
