from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/about/')
def about():
    return render_template("about.html")
 
@views.route('/profile/')
def profile():
    return render_template("profile.html")

@views.route('/behavioral/')
def bev():
    return render_template("behavorial.html")

@views.route('/technical/')
def tech():
    return render_template("technical.html")

@views.route('/company/')
def comp():
    return render_template("company.html")
