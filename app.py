
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return redirect(url_for("home"))

    username = request.form.get("username")
    password = request.form.get("password")

    if username == "kowshik"  and password == "1":
     return redirect(url_for("success"))
    

    return render_template("login.html", error="Invalid Username or Password")


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)