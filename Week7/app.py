import json
import mysql.connector
# set infos to connect to database
MysqlConnectInfo = {
	"user" : "root",
	"password" : "root123",
	"host" : "localhost",
	"database" : "website"
}

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

@app.route("/signup", methods = ["POST"])
def signup():
	Name = request.form["Name"]
	Username = request.form["Username"]
	Password = request.form["Password"]

	con = mysql.connector.connect(**MysqlConnectInfo)
	cursor = con.cursor()
	# "COLLATE utf8mb4_bin" for comparing letter case
	cursor.execute("SELECT * FROM member WHERE username = %s COLLATE utf8mb4_bin",(Username, ))
	data = cursor.fetchone()

	# Check if uesrname dosen't exist
	if data == None:
		cursor.execute("INSERT INTO member(name, username, password) VALUES(%s, %s, %s)",(Name, Username, Password))
		con.commit()
		con.close()
		return redirect("/")

	con.close()	
	return redirect("/error?message=帳號已被註冊")
	
@app.route("/signin", methods = ["POST"])
def signin():
	Username = request.form["Username"]
	Password = request.form["Password"]

	con = mysql.connector.connect(**MysqlConnectInfo)
	cursor = con.cursor(dictionary = True)
	cursor.execute("SELECT * FROM member WHERE username = %s and password = %s COLLATE utf8mb4_bin",(Username, Password))
	data = cursor.fetchone()
	con.close()

	# Check if username or password not matched
	if data == None:
		return redirect("/error?message=帳號或密碼錯誤")

	# Record user status
	session["id"] = data["id"]
	session["name"] = data["name"]
	session["username"] = data["username"]
	return redirect("/member")

@app.route("/signout")
def signout():
	session.pop("id",None)
	session.pop("name",None)
	session.pop("username",None)
	return redirect("/")

@app.route("/member")
def member():
	# Check user status
	if "name" in session:
		con = mysql.connector.connect(**MysqlConnectInfo)
		cursor = con.cursor(dictionary = True)
		cursor.execute("SELECT message.member_id, member.name, message.content, message.id FROM message INNER JOIN member ON member.id = message.member_id ORDER BY message.time DESC")
		data = cursor.fetchall()
		con.close()
		return render_template("member.html", Name = session["name"], SessionId = session["id"], MsgData = data)
	
	return redirect("/")

@app.route("/error")
def error():
	ErrMsg = request.args.get("message","")
	return render_template("error.html", Msg = ErrMsg)

@app.route("/createMessage", methods = ["POST"])
def createMessage():
	MsgContent = request.form["MsgContent"]

	con = mysql.connector.connect(**MysqlConnectInfo)
	cursor = con.cursor()
	cursor.execute("INSERT INTO message(member_id, content) VALUES(%s,%s)",(session["id"], MsgContent))
	con.commit()
	con.close()

	return redirect("/member")

@app.route("/deleteMessage", methods = ["POST"])
def deleteMessage():
	DelMsgId = request.form["DelMsgId"]

	con = mysql.connector.connect(**MysqlConnectInfo)
	cursor = con.cursor()
	cursor.execute("DELETE FROM message WHERE id = %s",(DelMsgId,))
	con.commit()
	con.close()
	return redirect("/member")

@app.route("/api/member", methods = ["GET", "PATCH"])
def api_member():
	if request.method == "GET":
		return FindName()
	elif request.method == "PATCH":
		return ChangeName()

def FindName():
	Username = request.args.get("username","")
	result = {}
	if "name" not in session:
		result["data"] = None
	else:
		try:
			con = mysql.connector.connect(**MysqlConnectInfo)
			cursor = con.cursor(dictionary = True)
			cursor.execute("SELECT id, name, username FROM member WHERE username = %s",(Username,))
			data = cursor.fetchone()
			con.close()
	
			if data == None:
				result["data"] = None
			else:
				result["data"] = data
		except mysql.connector.Error:
			result["data"] = None
	return json.dumps(result,ensure_ascii = False)

def ChangeName():
	NewName = request.get_json()["name"]
	result = {}
	if "name" not in session:
		result["error"] = True
	else:
		try:
			con = mysql.connector.connect(**MysqlConnectInfo)
			cursor = con.cursor()
			cursor.execute("UPDATE member SET name = %s WHERE id = %s",(NewName, session["id"]))
			con.commit()
			con.close()
			result["ok"] = True
			session["name"] = NewName
		except mysql.connector.Error:
			result["error"] = True

	return json.dumps(result)

app.run(port = 3000)