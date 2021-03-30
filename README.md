# REST-API

## To do
- Test the app on AWS
- Add https functionality - by Nishant 
- README update and code comments

## Running the app locally

#### install packages
``` pip install -r requirements.txt ```

#### start flask server
``` python run.py ```

#### open swagger docs in the brower by fllowing the base url

## Using docker
#### Start your EC2 instance
#### Update the system and install docker 
```sudo apt update```
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
