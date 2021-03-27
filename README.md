# REST-API

## Activate virtual env 
``` source .env/bib/activate ```

## install packages
``` pip install -r requirements.txt ```
## db setup
``` export FLASK_APP=run.py ```
``` flask db init ```
``` flask db migrate ```
``` flask db upgrade ```

## load db with sample users along with admin
``` python add_users.py ```

## start flask server
``` python run.py ```

### open swagger docs in the brower by fllowing the base url

### To do
- My SQL db setup
- Dockerize application
- Add https functionality
