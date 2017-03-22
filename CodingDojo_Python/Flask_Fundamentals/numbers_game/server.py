from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Secret'
import random


	

@app.route('/')
def index():
	random_num = random.randrange(0,101)
	if 'num' not in session:
		session ['num'] = random_num
	print random_num
	return render_template("index.html")

@app.route ('/guess', methods=['POST'])
def guess():
	guess = request.form['guess']
	guess = int(guess)

	if guess < session['num']:
		session['fail'] = "Too Low"
	elif guess > session['num']:
		session ['fail'] = "Too High"
	else: 
		if 'fail' in session:
			session.pop('fail')
		session['success'] = "The number was {}. You guessed it correctly".format(session['num'])
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear
	return redirect('/')




app.run(debug=True) 