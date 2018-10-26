from flask import Flask, Request, json, jsonify, request
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)

from app import app
from storeapi.models.sales_model import Sale
from storeapi.models.user_model import User, attendant,admin

# app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'andela13' 

jwt = JWTManager(app)


sale=Sale()
attendant = User(2,'attendant','password', False)

@app.route('/api/v1/sales',methods=['POST'])
@jwt_required
def add_sale_order():
    current_user = get_jwt_identity()
    if current_user == 'attendant':
        return sale.add_sale()
    return jsonify({"message":"Access denied, Log in as attendant to add sale orders."}), 401

@app.route('/api/v1/sales/<int:saleId>', methods=['GET'])
def fetch_a_sale_order(saleId):
    return sale.fetch_sale(saleId)
    
@app.route('/api/v1/sales', methods=['GET'])
@jwt_required
def fetch_all_sale_orders():
    current_user = get_jwt_identity()
    if current_user == 'admin':
       return sale.get_sales()
    return jsonify({"message":"Access denied, Log in as admin to fetch all sale orders."}), 401