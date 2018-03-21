from flask import Flask, request, make_response, render_template
import uuid

app = Flask(__name__)

username = str(uuid.uuid4())
password = str(uuid.uuid4())

@app.route("/", methods=["get", "post"])
def database():
    print(request.method)
    if request.method == "GET":
        response = make_response(render_template("database.html"))
        response.headers["X-Auth-Username"] = username
        response.headers["X-Auth-Password"] = password
        return response
    elif request.method == "POST":
        if "username" in request.form and \
           "password" in request.form and \
           request.form["username"] == username and \
           request.form["password"] == password:
            return render_template("winner.html")
        return "no"

if __name__ == "__main__":
    app.run(debug=True)
