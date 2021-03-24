from flask import Flask, jsonify, json, request
import mysql.connector
from passlib.hash import sha256_crypt

app = Flask(__name__)

# create a connection to the database
def create_connection():
    """ create a database connection to the mySQL database
    :return: Connection object or None
    """
    conn = mysql.connector.connect(
        host="group17-githubjobs.cbgj5urfzqbw.us-east-1.rds.amazonaws.com",
        user="group17Admin",
        password="Group17Password",
        database="JobSearchAPI"
    )
    return conn

# just an example GET call for table user
@app.route('/users', methods=['GET'])
def get_all_users():
    mycursor.execute("SELECT * FROM user")
    myresults = mycursor.fetchall()
    return jsonify(myresults), 200

# register a new user
@app.route('/register', methods=['POST'])
def register_user():
    # check that the request contains 7 arguments
    if len(request.args) != 7:
        return jsonify({'error':'Not all arguments required have been included'}), 400
    else:
        # prepare a list of arguments for login table
        # use hashing to encrypt the password
        user_login = (request.args['username'], sha256_crypt.hash(request.args['password']))
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
        user_user = (id_number, request.args['name'], request.args['email'], 0, request.args['keyword'], request.args['full_time'], request.args['location'])
        # sql code for inserting a new user into user table
        sql_user = '''INSERT INTO user(user_id, name, email, admin, keyword, full_time, location)
                    VALUES(%s,%s,%s,%s,%s,%s,%s) '''
        # execute the query
        mycursor.execute(sql_user, user_user)
        conn.commit()
        return jsonify({'message':f"New user added, username: {request.args['username']}"}), 201

if __name__ == '__main__':
    conn = create_connection()
    mycursor = conn.cursor()
    app.run(debug=True)