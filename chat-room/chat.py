

from flask import Flask, jsonify
from flask import send_from_directory
from flask import request

app = Flask(__name__)


class User:
    def __init__(self,username,email,password):
        self.username = username    
        self.email = email
        self.password = password
    

class Message:
    def __init__(self, sender : User, content : str):
        self.sender = sender
        self.content = content

    
class ChatRoom:
    def __init__(self, username):
        self.username = username  
        self.massages = []  

    def add_message(self,message):
        pass # TODO:



# TODO1: make users persistent with a file based user list 
users = []
# TODO1: load all users from json file



chat_rooms = []


def unique_user(email,username):
    """ check if username and email is unique """
    for u in users:
        if u.email == email or u.username == username :
            return False
    return True    


@app.route("/api/room/<id>")
def room_chats(id):
    return "no room implimentd"


@app.route("/api/sign-up")
def signup():
    username = request.args.get('username') 
    email = request.args.get('email') 
    password = request.args.get('password') 
    if not unique_user(email,username) :
        return 'username of email alredy exist!', 409
    if email==None or email == None or password==None:
        return 'bad request!', 400
    
    users.append(User(username,email,password))
    # TODO1: save all users to json file


    return jsonify("user created!")


@app.route("/api/see-all-users")
def all_users():
    users_dictionary = []
    for u in users:
        users_dictionary.append({
            "username":u.username,
            "email":u.email
        })
    return jsonify(users_dictionary)
    


@app.route("/<path>")
def static_files(path):
    extention = path.split(".")[-1]
    if extention in ["html","css","js","ogg"]:
        return send_from_directory('static', path )
    else:
        return send_from_directory('static', path + ".html")


@app.route("/")
def home():
    return send_from_directory('static', "index.html")


app.run(host='0.0.0.0', port=5000, debug=True)


