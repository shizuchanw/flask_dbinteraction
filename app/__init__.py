from flask import Flask, render_template, request
from .app import insert_message, random_messages

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("base.html")

@app.route("/submit/", methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template("submit.html")
    else:
        insert_message(request)
        return render_template("submit.html", thanks = True)

@app.route("/view/")
def view():
    msg = random_messages(5)
    return render_template("view.html", messages = msg)

