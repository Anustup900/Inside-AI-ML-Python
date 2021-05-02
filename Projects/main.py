import flask 

from flask import Flask, render_template 


app = Flask(__name__)


@app.route("/")
def landingpage():
    return render_template("normal.html")


@app.route("/aiml")
def aimlpage():
    return "aiml page"

@app.route("/anustup")
def anustuppage():
    return "I am anustup, a machine learning instructor"

if __name__ == "__main__":
    app.run(debug = True)