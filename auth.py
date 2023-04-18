# login
from flask import Blueprint, render_template, url_for, request, redirect

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    print(email, password)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')
    
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    print(email, username, password)
    
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return "Logged Out!"