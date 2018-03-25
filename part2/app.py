from flask import Flask, request, make_response, render_template, session, url_for, redirect, flash, send_from_directory

import uuid

app = Flask(__name__)
app.secret_key = "5d477e99-df8b-4961-b73a-c82fa8e167b1"

username = str(uuid.uuid4())
password = str(uuid.uuid4())
answer = "something!"

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

@app.route("/login", methods=["get", "post"])
def login():
    def login_page():
        response = make_response(render_template("login.html"))
        response.headers["X-NODONTLOOKHERE-USERNAME"] = username
        response.headers["X-NOISAIDLEASEDONTLOOKHERE-PASSWORD"] = password
        return response

    if "username" in session:
        return "You're already logged in silly"

    if request.method == "GET":
        return login_page()
    elif request.method == "POST":
        if "username" in request.form and \
           "password" in request.form and \
           request.form["username"] == username and \
           request.form["password"] == password:
            session["username"] = request.form["username"]
            return redirect(url_for("database"))
        else:
            flash("NOPE!!!")
            return login_page()

@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Successfully logged out")
    return redirect(url_for("dashboard"))

@app.route("/winner")
def winner():
    if "username" not in session:
        return redirect(url_for("login"))

    if "winner" not in session:
        return "no"

    return render_template("winner.html")

@app.route("/database", methods=["get", "post"])
def database():
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "GET":
        return render_template("database.html")

    if "answer" in request.form and request.form["answer"] == answer:
        session["winner"] = "yep"
        return redirect(url_for("winner"))
    else:
        flash("NOPE!!!")
        return render_template("database.html")

if __name__ == "__main__":
    app.run(debug=True)
