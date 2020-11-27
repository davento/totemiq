from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/"):
def index():
	return render_template("home.html")

@app.route("/login"):
def login():
	#Handle login (if we are gonna do that)	

if __name__ == "__main__":
	app.run(debug=True)