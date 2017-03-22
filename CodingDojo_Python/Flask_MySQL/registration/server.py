from flask import Flask, redirect, request, session, render_template, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector
import re

email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

app = Flask(__name__)
app.secret_key = 'Secret'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'registration')




@app.route('/')
def index():
	return render_template('index.html')


@app.route('/register', methods =['POST'])
def register():
	errors = []

	if len(request.form['first_name']) < 2:
		errors.append('First name must be at least 2 characters long.')

	if len(request.form['last_name']) < 2:
		errors.append('Last name must be at least 2 characters long.')

	if not len(request.form['email']) < 2:
		errors.append('Email required.')

	if len(request.form['passsword']) < 8:
		errors.append('Password name must be at least 8 characters long.')

	if len(request.form['password_confirmation']) < 2:
		errors.append('Password confirmation must be at least 8 characters long.')

	
	if not request.form['password'] == request.form['password_confirmation']:
		errors.append('Password fields must match.')

	if not email_regex.match(request.form['email']):
		errors.append('Please enter a valid email.')

	else: 
		
		query = "SELECT * FROM users WHERE email = :email"
		data = {
			'email': request.form['email']
		}

		if mysql.query_db(query, data):
			errors.append('Email already registered.')
			print errors

	if not errors:
		hashed_password = bcrypt.generate_password_hash(request.form['password'])

		query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :hashed_pw, NOW(), NOW())"

		data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'fm_email': request.form['email'],
			'hashed_pw': hashed_password
		}

		user_id = mysql.query_db(query, data)
		session['user_id'] = user_id

		return redirect('/success')

	else:
		for errors in errors:
			flash(error)
			print error
		return redirect('/')


@app.route('/login', methods=['POST'])
def login():

	query = 'SELECT * FROM users WHERE email = :email'
	data = {
		'email': request.form['email']
	}

	user = mysql.query_db(query, data)

	if not user:
		flash('Please enter a valid email address')

		return redirect('/')

	else:
		if not len(request.form['password']):
			flash('Must provide password.')
			
			return redirect('/')
		
		if bcrypt.check_password_hash(user[0]['password'], request.form['password']):
			session['user_id'] = user[0]['id']

			return redirect('/success')

		else:
			flash('Invalid email/password combination')

			return redirect('/')


@app.route('/success')
def success():

	if not 'user_id' in session:
		flash('Must be logged in')
		return redirect('/')

	query = 'SELECT first_name, last_name FROM users WHERE id = session_user_id'
	data = {
		'session_user_id': session['user_id']
	}

	user = mysql.query_db(query, data)

	return render_template('success.html', logged_in_user = user[0])
	

@app.route('/delete', methods=['POST'])
def delete():
	session.clear()
	return redirect('/')


app.run(debug=True)