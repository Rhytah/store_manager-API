from flask import Flask,json,request, jsonify

from .models import Product, products, User, Sale,sale_orders,a_product,a_sale_order

app= Flask(__name__)

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
    # if len(products) <1:
    #     return jsonify ({
    #         "status":"Fail",
    #         "message":"No products in inventory"
    #     }),404

    if len(products) >1:
        return jsonify({
            "message":"Available Products",
            "Products":products
        }),200
    
    return jsonify({"Error":"Products not found "})


@app.route('/api/v1/products/<int:productId>',methods=['GET'])
def fetch_a_specific_product(productId):
    if len(products) <1:
        return jsonify ({
            "Status":"Fail", 
            "message":"No products in inventory"
            }),404


    for a_product in products:
        if a_product['productId']==productId:
            return jsonify({
                "message":"You have fetched product",
                "Product":a_product
            }),200

    return jsonify({
        "Error":"Product not found , check to see that you wrote the right ID"
        })

@app.route('/api/v1/attendant/sales',methods=['POST'])
def add_sale_order():
    sale_data=request.get_json()
    saleId=len(sale_orders)+1
    productName=sale_data.get('productName')
    created_by=sale_data.get('created_by')
    details =sale_data.get('details')

    new_sale_order={'saleId':saleId, 'productName':productName, 'created_by':created_by,'details':details}
    sale_orders.append(new_sale_order)

    return jsonify({"message":"You have successfully created a sale order"}),200


@app.route('/api/v1/sales/<int:saleId>', methods=['GET'])
def fetch_a_sale_order(saleId):
    if len(sale_orders)<1:
        return jsonify({
            "status":"Fail",
            "message":"NO sale orders at the moment"
        }),404

    
    for a_sale_order in sale_orders:
        if a_sale_order['saleId']==saleId:
            return jsonify({
                "message":"You have fetched a sale order",
                "Sale_order":a_sale_order
            }),200
    
    return jsonify({"Error":"Order not found , check to see that you wrote the right ID"})


@app.route('/api/v1/admin/sales', methods=['GET'])
def fetch_all_sale_orders():
    if len(sale_orders) <1:
        return jsonify ({
            "status":"Fail",
            "message":"No sale orders at the moment"
        }),404

    if len(sale_orders) >1:
        return jsonify({
            "message":"Sale orders",
            "Sales":sale_orders
        }),200

    return jsonify({"Error":"Orders not found "})
