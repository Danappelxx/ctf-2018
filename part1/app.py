from flask import Flask, request, render_template, redirect, session, flash, url_for, send_from_directory
from db import DB
from encoder import encode
import subprocess

app = Flask(__name__)
app.secret_key = "5029C3CE-04E5-42B1-AB81-30D2C121ABBC"

db = DB()
database_url = "http://losaltoshacks3.westus2.cloudapp.azure.com:8000/database"

# statics
@app.route("/css/<path:path>")
def css(path):
    print(path)
    return send_from_directory("../static/css", path)
@app.route("/js/<path:path>")
def js(path):
    return send_from_directory("../static/js", path)
@app.route("/fonts/<path:path>")
def fonts(path):
    return send_from_directory("../static/fonts", path)

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    if db.is_admin(session["username"]):
        return render_template("dashboard.html", adminsection="<a href='{}'><h2>database</h2></a>".format(database_url))

    return render_template("dashboard.html")

@app.route("/apply", methods=["get", "post"])
def apply():
    if request.method == "GET":
        return render_template("apply.html")
    elif request.method == "POST":
        # log the user out if they arent already
        session.pop("username", None)

        username = request.form["username"]
        password = request.form["password"]
        password_hash = encode(password)
        if not db.create_user(username, password_hash):
            flash("User with same name already exists")
        return redirect(url_for("login"))

@app.route("/login1", methods=["get", "post"])
def login():
    if "username" in session:
        return redirect(url_for("dashboard"))

    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password_hash = encode(password)

        user = db.get_user(username)
        if user is not None and user["password_hash"] == password_hash:
            session['username'] = request.form['username']
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials")
            return render_template("login.html")

@app.route("/logout1")
def logout():
    session.pop("username", None)
    flash("Successfully logged out")
    return redirect(url_for("dashboard"))

@app.route("/calculate", methods=["post"])
def calculate():
    expression = request.json["input"]
    script = "exec(\"{}\")".format(expression)
    print(script)
    try:
        output = subprocess.check_output(["python2.7", "-c", script], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as error:
        # this is the error output of the script.
        # if we want to be nice, we could do
        # output = error.output.decode()
        # but that would make it too easy
        print(error.output.decode())
        output = "error"
    return output

if __name__ == "__main__":
    app.run()
