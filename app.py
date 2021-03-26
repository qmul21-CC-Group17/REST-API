from flask import Flask, jsonify, json, request, url_for, session
import mysql.connector
import requests
from passlib.hash import sha256_crypt
import re

app = Flask(__name__)
# secret key for maintaining sessions
app.secret_key = "super secret key"

# create a connection to the database
def create_connection():
    """ create a database connection to the mySQL database
    :return: Connection object or None
    """
    conn = mysql.connector.connect(
        host="group17-githubjobs.cbgj5urfzqbw.us-east-1.rds.amazonaws.com",
        user="", # login required
        password="", # password required
        database="JobSearchAPI"
    )
    return conn

# register a new user
@app.route('/register', methods=['POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if 'username' in request.args and 'password' in request.args and 'email' in request.args and 'name' in request.args and 'location' in request.args and 'full_time' in request.args and 'keyword' in request.args:
        # Create variables for easy access
        username = request.args['username']
        password = request.args['password']
        email = request.args['email']
        mycursor.execute('SELECT * FROM login WHERE username = %s', (username,))
        account = mycursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            # prepare a list of arguments for login table
            # use hashing to encrypt the password
            user_login = (username, sha256_crypt.hash(password))
            # sql code for inserting a new user into login table
            sql_login = '''INSERT INTO login(username,password)
                    VALUES(%s,%s)'''
            # execute the query
            mycursor.execute(sql_login, user_login)
            # commit the change
            conn.commit()
            # get the id of the newly inserted user
            # this will be reused to insert into the next table
            id_number = mycursor.lastrowid

            # prepare a list of arguments for user table    
            user_user = (id_number, request.args['name'], email, 0, request.args['keyword'], request.args['full_time'], request.args['location'])
            # sql code for inserting a new user into user table
            sql_user = '''INSERT INTO user(user_id, name, email, admin, keyword, full_time, location)
                    VALUES(%s,%s,%s,%s,%s,%s,%s) '''
            # execute the query
            mycursor.execute(sql_user, user_user)
            conn.commit()
            msg = 'You have successfully registered!'
            return jsonify({'message':msg}), 201
    else:
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Return any error messages
    return jsonify({'message': msg}), 400

@app.route('/login', methods=['POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.args and 'password' in request.args:
        # Create variables for easy access
        username = request.args['username']
        password = request.args['password']
        # Check if account exists SQL

        mycursor.execute('SELECT * FROM login WHERE username = %s', (username,))
        # Fetch one record and return result
        account = mycursor.fetchone()
        # If account exists in accounts table in out database
        if account and sha256_crypt.verify(password, account[2]):
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            # Check if the user is an admin
            mycursor.execute('SELECT user_id, admin FROM user WHERE user_id = %s', (session['id'],))
            user_admin = mycursor.fetchone()
            session['admin'] = user_admin[1]
            # get the no of time logged in
            mycursor.execute('SELECT user_id, login_count FROM login WHERE user_id = %s', (session['id'],))
            user_login = mycursor.fetchone()
            login_number = user_login[1]
            login_number += 1
            # create a variable for date
            #today = str(date.today())
            # update the table
            mycursor.execute('UPDATE login SET login_count = %s, last_login = NOW() WHERE user_id = %s', (login_number, session['id'],))
            conn.commit()
            # The user has been logged in
            msg = f'Logged in successfully!'
            return jsonify({'message': msg}), 200
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
            return jsonify({'message': msg}), 401
        
@app.route('/logout', methods=['GET'])
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('admin', None)
    # Redirect to login page
    msg = "Logged out."
    return jsonify({'message': msg}), 200

# if admin, get all users
@app.route('/admin/users', methods=['GET'])
def get_all_users():
    if session['admin'] == 1:
        mycursor.execute("""SELECT login.user_id, login.username, \
            login.login_count, login.last_login, \
            user.name, user.email, user.admin, user.keyword, \
            user.full_time, user.location \
            FROM login \
            INNER JOIN user ON login.user_id = user.user_id""")
        myresults = mycursor.fetchall()
        return jsonify(myresults), 200
    else:
        msg = "Only admins can access this resource"
        return jsonify({'message': msg}), 400

# if admin, amend user details
@app.route('/admin/amend_user', methods=['PUT'])
def admin_amend_user():
    if session['admin'] == 1:
        #TODO
        msg = "TODO"
        return jsonify(myresults), 200
    else:
        msg = "Only admins can access this resource"
        return jsonify({'message': msg}), 400

# amend user details
@app.route('/amend_user', methods=['PUT'])
def amend_user():
    #check if the user is logged in
    id = session['id']
    email = request.form['email'] #new email
    keyword = request.form['keyword']#new keyword
    location = request.form['location']#new location
    mycursor.execute('UPDATE user SET email = %s, keyword = %s, location = %s WHERE user_id = %d', (email, keyword, location, id))
    mysql.connection.commit()
    msg = 'successfully updated!'
        return jsonify({'message':msg}), 200

# delete an account
@app.route('/delete_account', methods=['DELETE'])
def delete_account():
    id = session.pop(id, None)
    mycursor.execute('DELETE FROM user WHERE user_id = %d',(id))
    mysql.connection.commit()
    msg = 'successfully deleted!'
        return jsonify({'message':msg}), 200

# get jobs
# includes the use of externap API
@app.route('/get_jobs', methods=['GET'])
def get_jobs():
    msg = 'login required'
    if session['loggedin'] == True:
        job_template = 'https://jobs.github.com/positions.json?description={job}&location={loc}&full_time={fu}'
        mycursor.execute('SELECT * FROM user WHERE user_id = %s', (session['id'],))
        get_job = mycursor.fetchone()
        location = get_job[6]
        location = location.replace(" ","+")# replaces any blank spaces with + character so it works in the URL format
        desc = get_job[4]
        desc = desc.replace(" ","+") # replaces any blank spaces with + character so it works in the URL format
        ft =  get_job[5] # can take values 'on' and 'off'
        job_url = job_template.format(job = desc, loc = location, fu = ft)
        resp = requests.get(job_url)
        if resp.ok:
            if len(resp.json()) == 0:
                return jsonify({'message': 'No jobs found'}), 200
            else:
                return jsonify(resp.json()), 200
        else:
            print(resp.reason)
    else: 
         return jsonify({'message': msg}), 400

if __name__ == '__main__':
    conn = create_connection()
    mycursor = conn.cursor()
    app.run(debug=True)
