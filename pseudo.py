username = request.form['username'] 
password = request.form['password']
verify_password = request.form['verify_password']

#If the user's form submission is not valid, you should reject it and re-render the form 
#with some feedback to inform the user of what they did wrong. 


#The following things should trigger an error:


#1) The user leaves any of the following fields empty: username, password, verify password.
    if len(username) == 0:
        return <h2> Invalid Username </h2>
    if len(password) == 0:
        return <h2> Passwords cannot be empty </h2>
    if len(verify_password) == 0:
        return <h2> Passwords cannot be empty </h2>  


#2) The user's username or password is not valid: 
#          it contains a space character or 
    if username == " "
        return <h2> Username cannot contain spaces"
    if password == " "
        return <h2> Passwords cannot contain spaces"
    if verify_password == " "
        return <h2> Passwords cannot contain spaces"


#          it consists of less than 3 characters or more than 20 characters
    if len(username) < 3: or len(username) > 20:
        return <h2> Username must be greater than 3 and less than 24 characters </>
    if len(password) < 3: or len(password) > 20:
        return <h2> password must be greater than 3 and less than 24 characters </>
    if len(username) < 3: or len(username) > 20:
        return <h2> Username must be greater than 3 and less than 24 characters </>



#3) The user's password and password-confirmation do not match.
    if password != verify_password:
        return <h2>Passwords must match"</h2>

#4) The user provides an email, but it's not a valid email. 
#   Note: the email field may be left empty, but if there is content in it:
    if len(email) > 0:
        if "@" not in email or "." not in email:
            return<h2>Email must contain '@' and '.'</h2>

#        then it must be validated:
#           has a single @, 
#           a single ., 
#           contains no spaces, 
#           and is between 3 and 20 characters long.

# Each feedback message should be next to the field that it refers to.

#For the username and email fields, you should preserve what the user typed, 
#so they don't have to retype it. With the password fields, you should clear them, 
#for security reasons.

return redirect("/")

#Use templates (one for the index/home to render the HTML for your web app.
@app.route('/')


#If all the input is valid, then you should show the user a welcome page 
#that uses the username input to display a welcome message of: "Welcome, [username]!"
@app.route('/welcome')