
from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

username = request.form['username'] 
password = request.form['password']
verify_password = request.form['verify_password']
email = request.form['email']

@app.route("/")
def index():
    return render.template('signup_form.html') 

@app.route("/welcome", methods =['POST'])
def welcome():
    return render_template('hello_greeting.html', name=username)

@app.route('/validate_username')
def not_valid():
    return render_template('validate_username.html')



