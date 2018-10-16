from flask import Flask,json,request, jsonify

from .models import Product, products, User, Sale,sale_orders

app= Flask(__name__)

@app.route('/', methods=['GET'])
def trya():
    return jsonify({"message":"it's working"})