from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Test script to see if I can get Heroku working


@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return """
    <h1>Successful!</h1>
    <p>Time is currently is currently {time}.</p>
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
