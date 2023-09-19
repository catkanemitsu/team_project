from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user # import entire file, rather than class, to avoid circular imports





#Create Users and sets them in session.
@app.route('/')
def create_page():
    return render_template('index.html')

@app.route('/create', methods = ["POST"])
def create_user():
    if user.User.create_user(request.form):
        return redirect('/home')
    return redirect ('/')
#Login Users and sets them in session
@app.route('/login')
def user_login_page():
    return render_template('login.html')

@app.route('/users/login' , methods = ['POST'])
def login():
    print("im here")
    if user.User.login(request.form):
        print(session['user_id'])
        return redirect('/home')
    return redirect('/login')

#Home route where dashboard will live.
@app.route('/home')
def index():
    if 'user_id' not in session :
        return redirect('/login')
    else:
        print(session['first_name'])
        return render_template('home.html')

#LOGOUT/ Clears session. Prototects the rest of the routes
@app.route('/users/logout')
def logout():
    session.clear()
    return redirect('/login')

# Update Users Controller


# Delete Users Controller
