
from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyD1emdOGhcPXh2GXORAxSJWnqAglVbbZQ0",
  "authDomain": "codesecond-d5135.firebaseapp.com",
  "projectId": "codesecond-d5135",
  "storageBucket": "codesecond-d5135.appspot.com",
  "messagingSenderId": "908026155682",
  "appId": "1:908026155682:web:3a2bbedecb71a218937dfb",
  "databaseURL": "https://codesecond-d5135-default-rtdb.europe-west1.firebasedatabase.app/"
}


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route('/' , methods = ["GET", "POST"])
def main():
    if request.method == "GET":
      return render_template("signup.html")

    Email = request.form['Email']
    Password = request.form['Password']
    full_name = request.form['full_name']
    username = request.form['username']

    login_session['Email'] = Email
    login_session['Password'] = Password
    login_session['full_name'] = full_name
    login_session['username'] = username
  try :
    login_session['user'] = auth.create_user_with_email_and_password(Email, Password)
    user_id = login_session['user']['localId']
    login_session['quotes']= []
    user = {"full_name" : full_name, "Email" : Email, "username" : username}
    user_id = login_session['user']['localId']
    db.child("users").child(user_id).set(user)
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
  if request.method == 'GET' :
    return render_template("signin.html")
  else :
    Email  = request.form['Email']
    Password = request.form['Password']
  try:
    login_session['user'] = auth.sign_in_with_email_and_password(Email, Password)
    return redirect(url_for('home'))
  except:
    error = "Authentication failed"
    print(error)
    return render_template("signin.html")

@app.route("/home", methods = ["GET", "POST"])
def home():
  if login_session['user'] != None :
    if request.method == "GET":
      return render_template('home.html')
      print('Hoba ya boba')
  else :
    quote = request.form['quote']
    said_by = request.form['said_by']
    # login_session['quotes'].append(quote)
    quote = {"text" : request.form["quote"], "said_by" : request.form["said_by"], "user_id": login_session['user']['localId']}
    db.child("quotes").push(quote)
    login_session.modified = True
    return render_template('thanks.html')

@app.route("/thanks", methods = ["GET", "POST"])
def thanks():
  if login_session['user'] != None :
    return render_template("thanks.html")
  else:
    return redirect(url_for('main'))

@app.route("/display", methods = ["GET", "POST"])
def display():
  if login_session['user'] != None :
    user_data = db.child("quotes").get().val()
    return render_template("display.html", user_data = user_data)
  else :
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)
