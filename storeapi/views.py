from flask import Flask, json, jsonify, request
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)

from .models import (Product, Sale, User, a_product, a_sale_order, products,
                     sale_orders)

app = Flask(__name__)


app.config['JWT_SECRET_KEY'] = 'andela13'  
jwt = JWTManager(app)

admin = User(1, 'admin','pass', True )
attendant = User(2,'attendant','password', False)

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
    
@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@app.route("/api/v1/products", methods =["POST"])
@jwt_required
def add_a_product():
    current_user = get_jwt_identity()
    if current_user == 'admin':
       
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
    return jsonify(message="Acess denied for non admins"), 401

@app.route('/api/v1/products', methods=['GET'])
def fetch_products():
    if len(products) <1:
        return jsonify ({
            "status":"Fail",
            "message":"No products in inventory"
        }),404

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

@app.route('/api/v1/sales',methods=['POST'])
@jwt_required
def add_sale_order():
    current_user = get_jwt_identity()
    if current_user == 'attendant':
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


@app.route('/api/v1/sales', methods=['GET'])
@jwt_required
def fetch_all_sale_orders():
    current_user = get_jwt_identity()
    if current_user == 'admin':
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
