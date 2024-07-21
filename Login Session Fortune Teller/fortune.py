from flask import Flask, render_template, url_for,redirect,request
from flask import session as login_session
import random

app = Flask(__name__,template_folder="templates", static_folder="static" )
app.config['SECRET_KEY'] = "Your_secret_string"
    
fortunes = [
    "You will soon embark on a journey that will lead to unexpected opportunities.",
    "A surprise gift will come your way, bringing joy and delight.",
    "An old friend will reach out to reconnect and reminisce about the past.",
    "You will discover a hidden talent that will bring you great satisfaction.",
    "A challenge you are facing will soon be resolved in your favor.",
    "New beginnings are on the horizon; embrace them with open arms.",
    "Good news will arrive when you least expect it.",
    "You will find clarity and peace in a situation that has been troubling you.",
    "A financial opportunity will present itself; seize it wisely.",
    "Your positive attitude will attract good fortune and happiness."
]
@app.route('/',  methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        print(login_session)
        login_session['realusername'] = username
        print(login_session)
        birthday1 = request.form['birthday1']
        login_session['birthday1'] = birthday1
        return redirect(url_for('home'))


@app.route('/home', methods=['GET', 'POST'])
def home():
    birthday1 = login_session.get('birthday1')
    birthday_month_length = len(birthday1)
    if request.method == 'GET':
        return render_template('fortune.html' , birthday_month_length = birthday_month_length,
            birthday1 = birthday1)
    else:
        birthday1 = request.form['birthday1']
        login_session['birthday1'] = birthday1
        birthday_month_length = len(birthday1) - 1
        return redirect(url_for("fortune", birthday_month_length = birthday_month_length,
            birthday1 = birthday1))




@app.route("/fortune/<int:birthday_month_length>", methods=["GET","POST"])
def fortune(birthday_month_length):
   
    if birthday_month_length < 10:

        # birth_month_length = b.len()
        fort = fortunes[birthday_month_length]
        #random.randint(0,10)] 
        return render_template('realfortune.html', fortt = fort, birthday_month_length=birthday_month_length)
    else:
        fort = "You have a bad fortune "
        return render_template('realfortune.html', fortt = fort, birthday_month_length=birthday_month_length)


if __name__ == '__main__':
    app.run(debug=True)