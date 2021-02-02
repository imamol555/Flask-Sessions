from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greetwithoutpost")
def greetwithoutpost():
    return render_template("greet.html", name=request.get.get("first_name", "Patil"))


@app.route("/greet", methods=["POST"])
def greet():
    return render_template("greet.html", name=request.form.get("first_name", "Patil"))


@app.route("/greetblock", methods=["POST"])
def greetblock():
    return render_template("greet.html", name=request.form.get("first_name", "Patil"))
