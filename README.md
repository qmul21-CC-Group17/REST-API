## To do
- Test the app on AWS
- Add https functionality - by Nishant 
- README update and code comments

# REST-API - JOB SEARCH WEB-APPLICATION

This application allows a user to create an account and search for full-time or part-time IT positions of any kind in any given location. The application makes use of the <b> GitHub Jobs Public API to return a JSON response of all the jobs for the given information.</b>
The app is <b>dockerized</b> and can be run on <b>AWS Server</b>. 

## Dynamic REST-API CRUD Operations: 
The REST API responses conform to REST standards and return appropriate messages along with <b>RESPONSE CODES.</b>

### GET
 - GET_JOBS method uses the external API and returns a list of jobs for the given parameters: job-name, location, full-time(true/false)
 - LIST_USERS method returns the list of users who have an account in the database used by the app. This method is only accessible by an ADMIN USER.
 
### POST 
- CREATE_USER method allows a user to register a new account with the webapp and therefore creates a new user in the user database with the following fields: username, password (encrypted hash using bcrypt algorithm), full-time (true/false), job-name, email and location. 

### PUT 
- UPDATE_USER method allows a logged in user to update their details namely: job-name, location, full-time and username. 

### DELETE
- DELETE_USER method allows a logged in user to delete their own account only.

## Interaction with External REST Service:
GET_JOBS method uses the <a href="https://jobs.github.com/api">GITHUB-JOBS API</a> to QUERY JOBS using the information provided by the user in the CREATE_USER POST method. THE API RETURNS A JSON RESPONSE of the list of jobs in the given location. This method can only be accessed after user_login. 

## External Cloud Database:
A remote access <b>MYSQL DATABASE hosted on AWS</b> is used by the web-application to store and retrieve persistent information such as: user details and blacklisted authorization tokens.

THE DATABASE consists of 2 TABLES:
 - USER TABLE consists of fields: id, username, email, password (hashed), keyword (job-name), full-time (true/false), location and Authorization(admin/user roles)
 - BLACKLISTED TABLE consists of fields: id (user id), token(JWT Token), blacklisted_on(time when token was added to table)

## Serving the Application over HTTPS:
- TO DO 

## Hash Based Authentication:
### B-CRYPT Hash Encrypted Passwords
When creating a user account, the password entered through POST method is first hashed by BCRYPT algorithm using a secret key and this hash is stored in the USER database. 
When a user is logging in, the user is AUTHENTICATED BY HASHING THE ENTERED PASSWORD AND COMPARING WITH THE HASH IN THE DATABASE, and only valid hashes are allowed to proceed.


## User Accounts and Access Management:
### JWT for Keeping Track of Sessions and Authorization
<b>JSON WEB TOKENS are generated every time a user registers or logs in</b>. This token is used to create a <b>SESSION</b> for the user that will last <b>upto 24-hours unless they logout</b>. This token is then used to access REST METHODS that require user login. <b>ONLY VALID TOKENS are authorized to perform CRUD operations</b>. Once the user is logged out, the TOKEN is <b> added to the list of blacklisted tokens</b> so that it may never be used again. Thus <b>securing the application.</b>

## Securing the Database with Role-Based Policies:
### ADMIN & USER Roles
- USER role is only allowed to access the method create__user, get_jobs, update_user to update their own details, and delete_user to delete ONLY THEIR OWN ACCOUNT. 
- ADMIN role is allowed to use the method list_users to see all the details of the user-role users who have accounts on the app. 
<b>THE ROLES AND THEIR AUTHORIZATION ARE VERIFIED BY THE 'Authorization' FIELD IN USER TABLE. THUS ONLY ADMIN HAS TRUE ACCESS TO THE USER DATABASE, THUS SECURING THE DATABASE. </b>
 ONE ADMIN ACCOUNT IS CREATED UPON RUNNING FIRST INSTANCE OF THE APP.

## Requirements: 
Python 3.8, Docker.io, Flask, Flask-Bcrypt, Flask-Migrate, flask-restx, 
Flask-Script, Flask-SQLAlchemy, PyJWT, requests, SQLAlchemy, 
mysqlclient, mysql-connector, pymysql


## Running the app locally

#### install packages
``` pip install -r requirements.txt ```

#### start flask server
``` python run.py ```

#### open swagger docs in the brower by fllowing the base url

## Using docker
#### Start your EC2 instance
#### Update the system and install docker 
```sudo apt update```<br>
```sudo apt install docker.io```
#### Move to the directory with the app
```cd REST-API-main```
#### Build the flask instance
```sudo docker build . --tag=flask:v1```
#### Run the instance
```sudo docker run -p 80:80 flask```
####Swagger docks should now be accessible via public DNS of the instance

## Setting the database for the first time
This only needs to be done once on an empty AWS RDS MySQL database
#### install packages
``` pip install -r requirements.txt ```
#### db setup
``` export FLASK_APP=run.py ```<br>
``` flask db init ```<br>
``` flask db migrate ```<br>
``` flask db upgrade ```<br>

#### load db with sample users along with admin
``` python add_users.py ```
