


from flask import Flask, jsonify
from flask import send_from_directory


app = Flask(__name__)


class User:
    def __init__(self,name,email,password):
        self.name = name    
        self.email = email
        self.password = password
    

class Message:
    def __init__(self, sender : User, content : str):
        self.sender = sender
        self.content = content

    
class ChatRoom:
    def __init__(self, name):
        self.name = name  
        self.massages = []  

    def add_message(self,message):
        pass # TODO:


# TODO: make data persistent! 

users = []
chat_rooms = []


def check_unique_user(email,name):
    """ check if user name and email is unique """
    for u in users:
        if u.email == email or u.name == name :
            return False
    return True    


@app.route("/api/room/<id>")
def room_chats(id):
    return "no room implimentd"



@app.route("/api/signUp")
def signup():
    #TODO: read from query-string params !
    #TODO: return error when need !
    name = "ali"
    email = "ali@ali.com"
    password = "123"
    users.append(User(name,email,password ))
    return jsonify("user created!")



@app.route("/api/see-all-users")
def all_users():
    user_names = []
    for u in users:
        user_names.append(u.name)
    return jsonify(user_names)
    


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


    

