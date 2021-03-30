# REST-API

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
- My SQL db setup - by Maciej
- Add https functionality - by Nishant 
- README update and code comments

### Using docker
- Build image
  ``` docker image build -t flask ```
- Run container
  ``` docker container run -v $(pwd):/app -p 5000:5000 flask ```


