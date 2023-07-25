from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session

app=Flask(__name__, static_folder = "public", static_url_path = "/")
app.secret_key = "ant string but secret"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/signin", methods = ["POST"])
def signin():
	Username = request.form["Username"]
	Password = request.form["Password"]
	if Username == "test" and Password == "test":
		# Record user status
		session["SIGNED-IN"] = True
		return redirect("/member")
	else:
		# Clear user status
		session["SIGNED-IN"] = False

		# Check error type
		if Username == "" or Password == "":
			return redirect("/error?message=Please enter username and password")
		else:
			return redirect("/error?message=Username or password is not correct")

@app.route("/signout")
def signout():
	session["SIGNED-IN"] = False
	return redirect("/")

@app.route("/member")
def member():
	# Check user status
	if "SIGNED-IN" in session:
		if session["SIGNED-IN"]:
			return render_template("member.html")
	
	return redirect("/")

@app.route("/error")
def error():
	ErrMsg = request.args.get("message","")
	return render_template("error.html", Msg = ErrMsg)

@app.route("/square")
def square():
	Number = int(float(request.args.get("Number","")))
	return render_template("square.html", Msg = (Number ** 2))

app.run(port = 3000)