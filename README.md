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
#### Build image
  ``` docker image build -t flask ```
#### Run container
  ``` docker container run -v $(pwd):/app -p 5000:5000 flask ```
#### open swagger docs in the brower by fllowing the base url

## Setting the database for the first time

#### install packages
``` pip install -r requirements.txt ```
#### db setup
``` export FLASK_APP=run.py ```<br>
``` flask db init ```<br>
``` flask db migrate ```<br>
``` flask db upgrade ```<br>

#### load db with sample users along with admin
``` python add_users.py ```
