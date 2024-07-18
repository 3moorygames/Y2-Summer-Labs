from flask import Flask, render_template, url_for,redirect,request
import random

app = Flask(__name__,template_folder="templates", static_folder="static" )
    
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


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('fortune.html')
    else:
        birthday = request.form['birthday1']
        birthday_month_length = len(birthday) - 1
        return redirect(url_for("fortune", birthday_month_length = birthday_month_length,
            b = birthday))



@app.route('/fortune/<int:birthday_month_length>')
def fortune(birthday_month_length):
    if birthday_month_length < 10:

        # birth_month_length = b.len()
        fort = fortunes[birthday_month_length]
        #random.randint(0,10)] 
        return render_template('realfortune.html', fortt = fort)
    else:
        fort = "You have a bad fortune "
        return render_template('realfortune.html', fortt = fort)


if __name__ == '__main__':
    app.run(debug=True)