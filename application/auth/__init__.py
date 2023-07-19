from flask import request, redirect, url_for, render_template
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user
from application import app

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.session_protection = "strong"

# Hardcoded database
users = {"test@test.com": {'password': 'qwerty'}}

class User(UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return

    user = User()
    user.id = username
    return user


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    if username not in users:
        return

    user = User()
    user.id = username
    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template("page_not_found.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in users and password == users[username]["password"]:
        user = User()
        user.id = username
        login_user(user)
        return redirect(url_for("home"))


    return render_template("index.html", error="invalid username or password"), 401


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
