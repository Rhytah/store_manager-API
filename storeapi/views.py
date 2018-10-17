from flask import Flask,json,request, jsonify

from .models import Product, products, User, Sale,sale_orders,a_product

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

@app.route('/api/v1/products', methods=['GET'])
def fetch_products():
    if len(products) <1:
        return jsonify ({
            "status":"Fail",
            "message":"No products in inventory"
        })

    if len(products) >1:
        return jsonify({
            "message":"Available Products",
            "Products":products
        }),200

@app.route('/api/v1/products/<int:productId>',methods=['GET'])
def fetch_a_specific_product(productId):
    if len(products) <1:
        return jsonify ({
            "status":"Fail",
            "message":"No products in inventory"
        })

    
    if len(products)>1:
        for a_product in products:
            if a_product['productId']==productId:
                return jsonify({
                    "message":"You have fetched product",
                    "Product":a_product
                }),200
        return jsonify({"Error":"Product not found , check to see that you wrote the right ID"})
