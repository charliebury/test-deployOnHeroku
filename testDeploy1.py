from flask import Flask
app = Flask(__name__)

# Test script to see if I can get Heroku working


@app.route('/doesThisWork')
def getRequestHello():
    return "Successful!"


if __name__ == '__main__':
    app.debug = True
    app.run()
