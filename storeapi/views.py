from flask import Flask,json,request, jsonify

from .models import Product, products, User, Sale,sale_orders

app= Flask(__name__)

@app.route('/', methods=['GET'])
def trya():
    return jsonify({"message":"it's working"})

@app.route("/api/v1/admin/products", methods =["POST"])
def add_a_product():
    request_data=request.get_json()
    productId=len(products)+1
    productName= request_data.get('productName')
    productPrice = request_data.get('productPrice')


    if not productName or productName =='  ' or productName == type(int):
        return({'message':"Product Name cannot be blank or a number"})

    if productPrice =="":
        return({'message':"Please insert digits"})

    new_product={"productId":productId,"productName":productName,"productPrice":productPrice}
    products.append(new_product)

    return jsonify({"message":f'Product {productName} successfully added'}),200
