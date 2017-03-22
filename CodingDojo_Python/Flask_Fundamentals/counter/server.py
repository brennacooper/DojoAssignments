from flask import Flask, render_template, request, redirect, session, random
app = Flask(__name__)
app.secret_key = 'Secret'

# def sumSessionCount():
# 	try:
# 		session['counter'] += 1
# 	except KeyError:
# 		session['counter'] =1

@app.before_first_request
def startup():
	session['counter'] = 0


@app.route('/')
def index():
	# sumSessionCount()
	session['counter'] += 1
	return render_template("index.html")



app.run(debug=True) 