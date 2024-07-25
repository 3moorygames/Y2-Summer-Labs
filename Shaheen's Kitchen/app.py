from flask import Flask, render_template, request, redirect, url_for
from flask import session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyAV-EvmshPc1ibcu4nBBazeNa9LVDk4-HQ",
  "authDomain": "shaheenkitchen-22c27.firebaseapp.com",
  "projectId": "shaheenkitchen-22c27",
  "storageBucket": "shaheenkitchen-22c27.appspot.com",
  "messagingSenderId": "267339712874",
  "appId": "1:267339712874:web:9b4e3e335c7a5b97b73d13",
  "databaseURL": "https://shaheenkitchen-22c27-default-rtdb.europe-west1.firebasedatabase.app/"
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

  session['Email'] = Email
  session['Password'] = Password
  try :
    session['user'] = auth.create_user_with_email_and_password(Email, Password)
    user_id = session['user']['localId']
    user = {"Email" : Email, "fav_foods": [] }
    user_id = session['user']['localId']
    db.child("users").child(user_id).set(user)
    return redirect(url_for("home"))
  except:
    print("error creating account")
    return render_template("signup.html")
@app.route("/signout", methods = ["GET", "POST"])
def signout():
  session['user']=None
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
    session['user'] = auth.sign_in_with_email_and_password(Email, Password)
    return redirect(url_for('home'))
  except:
    error = "Authentication failed"
    print(error)
    return render_template("signin.html")



@app.route("/home", methods = ["GET", "POST"])
def home():
  #if login_session['user'] != None :
    if request.method == "GET":
      return render_template('home.html')
    else:
      session.modified = True
      country = request.form['Region']
      session['Region'] = country
      
     
       

      return redirect(url_for('food',country=country))



@app.route("/food/<country>", methods = ["GET", "POST"])
def food(country):

  region = session['Region']
  if region == 'jordan':
      list_food = db.child(region).child('jordanian foods').get().val()
  elif region == 'palestine':
      list_food = db.child(region).child('palestinian_food').get().val()
  elif region == 'lebanon':
      list_food = db.child(region).child('lebanese foods').get().val()
  else:
      list_food = db.child(region).child('syrian food').get().val()

  if request.method == 'GET' :
    return render_template("region.html",country=country, foodlist=list_food)



 


@app.route("/thanks", methods = ["GET", "POST"])
def thanks():
  if session['user'] != None :
    return render_template("thanks.html")
  else:
    return redirect(url_for('main'))


@app.route("/recepie/<key>", methods = ["GET", "POST"])
def recepie(key):
  if request.method == "POST":
    user = db.child("users").child(session["user"]["localId"]).get().val()
    if "fav_foods" not in user or user["fav_foods"] is None:
      previous_fav_foods = []
    else:
      previous_fav_foods = user["fav_foods"]

    previous_fav_foods.append(key)
    db.child("users").child(session["user"]["localId"]).update({"fav_foods": previous_fav_foods})

  Recepies = {}
  list_foo = {}
  region = session['Region']
  if region == 'jordan':
    Recepies = db.child(region).child('jordanian foods').child(key).get().val()
    list_foo = db.child(region).child('jordanian foods').child(key).get().val()
  elif region == 'lebanon':
    Recepies = db.child(region).child('lebanese foods').child(key).get().val()
    print(Recepies)
    list_foo = db.child(region).child('lebanese foods').child(key).get().val()
    print(list_foo)
  elif region == 'palestine':
    Recepies = db.child(region).child('palestinian_food').child(key).get().val()
    list_foo = db.child(region).child('palestinian_food').child(key).get().val()
  else:
    Recepies = db.child(region).child('syrian food').child(key).get().val()
    list_foo = db.child(region).child('syrian food').child(key).get().val()

  return render_template('recepie.html', Recepies= Recepies, foodlis=list_foo, key=key)


@app.route("/favfoods", methods = ["GET", "POST"])
def favfood():

  if request.method == "POST":
    user = db.child("users").child(session["user"]["localId"]).get().val()
    if "fav_foods" not in user or user["fav_foods"] is None:
      print('pp')
      previous_fav_foods = []
      return render_template('favfood.html')
    previous_fav_foods = user["fav_foods"]
    if 'Remove' in request.form:
      Remove = request.form['Remove']
      print(Remove)
      if Remove in previous_fav_foods:
        previous_fav_foods.remove(Remove)
        db.child("users").child(session["user"]["localId"]).update({"fav_foods": previous_fav_foods})
    return render_template('favfood.html', previous_fav_foods = previous_fav_foods)
    # food_delete = request.form[""]

    # previous_fav_foods.remove(food_delete)
    # db.child("users").child(session["user"]["localId"]).update({"fav_foods": previous_fav_foods})



if __name__ == "__main__":
    app.run(debug=True)