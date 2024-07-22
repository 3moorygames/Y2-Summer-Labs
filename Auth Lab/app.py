
from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyA4l09b2jYmQxhchzZ7XolUbzS3Uo3mfWM",
  "authDomain": "auth-lab-ebf3c.firebaseapp.com",
  "projectId": "auth-lab-ebf3c",
  "storageBucket": "auth-lab-ebf3c.appspot.com",
  "messagingSenderId": "464680763",
  "appId": "1:464680763:web:7682447594a7a6e9f1691e",
  "databaseURL":""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/' , methods = ["GET", "POST"])
def main():
  if request.method == "GET":
    return render_template("signup.html")

  Email = request.form['Email']
  Password = request.form['Password']
    # login_session['Email'] = Email
    # login_session['Password'] = Password
    # login_session['quotes'] = []
  try :
    login_session['user'] = auth.create_user_with_email_and_password(Email, Password)
    login_session['quotes']= []
    return redirect(url_for("home"))
  except:
    print("error creating account")
    return render_template("signup.html")

@app.route("/signout", methods = ["GET", "POST"])
def signout():
  login_session['user']=None
  auth.current_user = None
  print("signed out user")
  return redirect(url_for('signin'))


@app.route('/signin', methods = ["GET", "POST"])
def signin():
  try:
    login_session['user'] = auth.sign_in_with_email_and_password(Email, Password)
    print(auth.create_user_with_email_and_password(Email, Password))
    return redirect(url_for('signin'))
  except:
    error = "Authentication failed"
    print(error)
    return render_template("signin.html")

@app.route("/home", methods = ["GET", "POST"])
def home():
  if request.method == "GET":
    return render_template('home.html')
  else :
    quote = request.form['quote']
    login_session['quotes'].append(quote)
    login_session.modified = True
    return render_template('thanks.html')

@app.route("/thanks", methods = ["GET", "POST"])
def thanks():
  return render_template("thanks.html")

@app.route("/display", methods = ["GET", "POST"])
def display():
  return render_template("display.html", quotes=login_session['quotes'])

if __name__ == "__main__":
    app.run(debug=True)
