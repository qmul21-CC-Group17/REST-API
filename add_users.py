from app.main.model.user import User
from app.main import db
from run import app

####Fill sample users into db along with admin for testing purposes. to be run the first time the app is installed. 


samples = [['Jyothsna', 'jyothsna@gamil.com', 'jyothsna123', 'cloud', True, 'London'],
        ['Maciej', 'maciej@yahoo.com', 'maciej123', 'development', True, 'Germany'],
        ['Ajay', 'ajay@gmail.com', 'ajay123', 'analyst', True, 'India'],
        ['Shreyas', 'shreyas@yahoo.com', 'shreyas123', 'python', True, 'sf'],
        ['Admin', 'admin@job_search.com', 'admin']]

attrs = ['username', 'email', 'password', 'keyword', 'full_time', 'location']
#adds the above sample users into the db then commits them. Sets admin value = true for user with the username Admin. 
def load_db():
    with app.app_context():
        User.query.delete()
        db.session.commit()
        for data in samples:
            user = User(**dict(zip(attrs, data)))
            if user.username=='Admin':
                user.is_admin = True
            db.session.add(user)
            db.session.commit()
        print(User.query.all())

if __name__=='__main__':
    load_db()
         
