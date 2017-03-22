from flask import Flask, request, redirect, render_template, session, flash

from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'Secret'
mysql = MySQLConnector(app,'emaildb')


def isValidEmail(email):
	if len(email) > 7:
		if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
			return True
	return False


@app.route('/', methods = ['GET','POST'])
def index():
	
		return render_template("index.html")

@app.route ('/validate', methods = ['GET','POST'])
def validate():
	email = request.form['email']
	errors = ''

	if isValidEmail(email)==True:
		query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    	data = 	{
    			'email': request.form['email']
   				 }
    	mysql.query_db(data, query)
    	return render_template("success.html", email=email)
		
		# else:
		# errors += "Email is not valid!"
		# return render_template("index.html", errors=errors)
	
	


@app.route('/success', methods=['POST'])

def success():  
    email = request.form['email']
    query = "SELECT email, DATE_FORMAT(created_at,'%m/%d/%y %h:%i%p') as date FROM users;"
    users = mysql.query_db(query)   
    # data = {
    #     	'email': request.form['email'], 
    #     	'date':  request.form['date'],
    # 		}
    return render_template('/success.html', email=email ,all_users=users)

app.run(debug=True)