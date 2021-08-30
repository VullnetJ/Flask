from flask import Flask



users = Flask(__name__)

@users.route('/')
def users():
    return '<h1>Hello World!</h1>'
@users.route("/users/home")
def userHome():
    return '<h1>Hello, {}!</h1>'.format(name)
    
# @users.route("/users/dosql")
# def doSQL():
    # db.create_all()