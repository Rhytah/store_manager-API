from flask import Flask, Request, json, jsonify, request
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)

from app import app
from storeapi.models.product_model import Product
from storeapi.models.user_model import User,admin

# app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'andela13' 


jwt = JWTManager(app)

product=Product()
admin = User(1, 'admin','pass', True )

@app.route("/api/v1/products", methods =["POST"])
@jwt_required
def add_products():

    current_user = get_jwt_identity()
    if current_user == 'admin':
        return product.add_a_product(),200
    return jsonify({"message":"Access denied, Log in as admin to add Products"}), 401

@app.route('/api/v1/products', methods=['GET'])
def fetch_products():
    product.get_products()   
    return ('Operation Success') 


@app.route('/api/v1/products/<int:productId>',methods=['GET'])
def fetch_a_specific_product(productId):
    return product.get_a_product(productId)

    