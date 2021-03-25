# REST-API

## The Database
The database for this project is hosted in AWS and is an RDS instance of MySQL database.<br>
The database consists of two tables:
- login:
  - user_id
  - username
  - password
  - login_count
  - last_login
- user:
  - user_id
  - name
  - email
  - admin
  - keyword
  - full_time
  - location
