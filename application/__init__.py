from flask import Flask, render_template
from flask_login import login_required

app = Flask(__name__)
app.secret_key = "APPLICATION_SECRET_KEY"


from application import auth

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
@login_required
def home():
    return render_template("home.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404
