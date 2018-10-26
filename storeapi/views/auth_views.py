from flask import Flask, json, jsonify, request
from app import app
from storeapi.models.user_model import User, admin,attendant
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)

app.config['JWT_SECRET_KEY'] = 'andela13'  
app.config['JWT_ACCESS_TOKEN_EXPIRES'] =False
jwt = JWTManager(app)


@app.route('/')
@app.route('/index')
def index():
    return "StoreManager App. Manage your Products and Sales efficiently"

@app.route('/api/v1/login', methods=["POST"])
def login():
    auth_data = request.get_json()
    username = auth_data.get("username")
    password = auth_data.get("password")
    access_token = create_access_token(identity=username)

    if not username and not password:
        return jsonify({"message":"enter your credentials"}), 401    

    if username == admin.username  and password == admin.password:     
        return jsonify ({"message":"logged in as admin", \
                        "access_token": access_token}), 200

    elif username == attendant.username and password == attendant.password:
        return jsonify({"message":"logged in as attendant",\
                        "access_token": access_token}), 200
    else:
        return jsonify ({"message":"Invalid username/password"}) , 401