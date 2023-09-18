from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user # import entire file, rather than class, to avoid circular imports





#Create Users
@app.route('/')
def create_page():
    return render_template('index.html')

@app.route('/create', methods = ["POST"])
def create_user():
    if user.User.create_user(request.form):
        return redirect('/home')
    return redirect ('/')
#Login Users
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

@app.route('/home')
def index():
    if 'user_id' not in session :
        return redirect('/login')
    else:
        print(session['first_name'])
        return render_template('home.html')

#LOGOUT
@app.route('/users/logout')
def logout():
    session.clear()
    return redirect('/login')

# Update Users Controller



# Delete Users Controller


# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')
# def index(id):
#     user_info = user.User.get_user_by_id(id)
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.
