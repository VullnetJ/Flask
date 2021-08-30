from flask import Flask

from flask_sqlalchemy import SQLAlchemy #class sqlachemy.
import pymysql

pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root@localhost8080:company"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app) #the class we imported

app.register_blueprint(users)


class Users(db.Model): #this creates a table
    #__tablename__ = "Pengunna" # to create a table name
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Unicode(80))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(40))

    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
db.create_all

new_user = People('Vullnet', 'info@google.com')

# db.session.add(People)
# db.session.commit() 
# db.session.add(new_user)
# db.session.commit()

result = db.engine.execute("SELECT * FROM People")
for person in results:
    print(person['people_name'])

