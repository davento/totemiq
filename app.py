from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/"):
def index():
	return render_template("index.html")

@app.route("/home"):
def home():
	#Handle main activity (display totemiq art)	

@app.route("/info"):
def info():
	#Handle display info about the proyect	

@app.route("/login"):
def login():
	#Handle login (if we are gonna do that)	

@app.route("/logout"):
def login():
	#Handle logout (if we are gonna do that)		

if __name__ == "__main__":
	app.run(debug=True)