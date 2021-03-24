import mysql.connector
from passlib.hash import sha256_crypt

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
    
def main():

    # create a database connection
    conn = create_connection()

    # set up a cursor object
    mycursor = conn.cursor()

    # sql for table for login
    sql_login = """CREATE TABLE login
                    (   user_id INT(11) NOT NULL AUTO_INCREMENT,
                        username VARCHAR(256) NOT NULL,
                        password CHAR(70) NOT NULL,
                        PRIMARY KEY (user_id)
                    ); """
    
    # create a table - only run once
    #mycursor.execute(sql_login)

    # insert the first admin user = run only once
    sql_insert_login = "INSERT INTO login (user_id, username,password) VALUES(%s, %s, %s)"
    val_login = (1, "admin", sha256_crypt.hash('admin'))
    #mycursor.execute(sql_insert_login, val_login)
    # get the id of the row to reuse later
    #id_value = mycursor.lastrowid

    # sql for table for user
    sql_user = """ CREATE TABLE IF NOT EXISTS user (
                        user_id INT(11) PRIMARY KEY,
                        name VARCHAR(256) NOT NULL,
                        email VARCHAR(256) NOT NULL,
                        admin BOOLEAN NOT NULL,
                        keyword VARChAR(256) NOT NULL,
                        full_time BOOLEAN NOT NULL,
                        location VARCHAR(256) NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES login (user_id)
                                    ); """
    
    # create a table - only run once
    #mycursor.execute(sql_user)

     # insert the first admin user - run only once
    sql_insert_user = """INSERT INTO user (user_id, name, email, admin, keyword, full_time, location)
                         VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    #val_user = (id_value, "Admin", "admin@admin.com", True, "Flask", True, "London")
    #mycursor.execute(sql_insert_user, val_user)
    
    # dropping a table
    #mycursor.execute("DROP TABLE user;")
    #mycursor.execute("DROP TABLE login;")

    # make the changes
    conn.commit()

    # print a list of tables
    print("A list of tables:")
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)
    
    # print the users in login
    print("Data in table login:")
    mycursor.execute("SELECT * FROM login")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    
    # print the users in user
    print("Data in table user:")
    mycursor.execute("SELECT * FROM user")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    # print data from both login and user using JOIN
    print("Data from both tables:")
    mycursor.execute("""SELECT login.user_id, login.username, \
            user.name, user.email \
            FROM login \
            INNER JOIN user ON login.user_id = user.user_id""")
    myresults = mycursor.fetchall()
    for x in myresults:
        print(x)

if __name__ == '__main__':
    main()