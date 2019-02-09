from flask import Flask, jsonify, request
from app.controllers.auth import Auth


app = Flask(__name__)
auth = Auth()

# the index route

@app.route('/api/v1')
def index():
    return jsonify({"Message":"Hello World !"})

# the auth route starts here

@app.route('/api/v1/auth/signup', methods=['POST']) 
def user_registration():
    data = request.get_json()
    return auth.signup(data)
    # pass
    # return jsonify({"Message":"User registration"})

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    return auth.login(data)
    # return jsonify({"Message":"User LogIn"})

@app.route('/api/v1/users')
def fetcha_all_users():
    return jsonify({"users":auth.get_users()})

# @app.route('/api/v1/checkuser')
# def find_users():
#     return auth.check_users()