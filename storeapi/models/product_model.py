from flask import jsonify, request
import re


products=[]
class Product:
    def ___init__(self, productId, productName,productPrice):
        self.productId=productId
        self.productName=productName
        self.productPrice=productPrice

        

    def add_a_product(self,*request_data):
        request_data=request.get_json()
        
        productId= len(products)+1
        productName= request_data.get('productName')
        productPrice = request_data.get('productPrice')

        if not productName:
            return "Product Name is missing"
        if productName == " ":
            return "Product Name is missing"
        if not re.match(r"^([a-zA-Z]+[-_\s])*[a-zA-Z]+$", productName):
            return "product name must have no white spaces"
        if not re.match(r"^[0-9]*$", productPrice):
            return "Product price must be only digits and must have no white spaces"    
        if len(productName) < 3:
            return "product name should be more than 4 characters long"
        if not productPrice:
            return "Product price is missing"
        if int(productPrice) < 1:
            return "Product price should be greater than zero"    
        if productPrice == " ":
            return "Product price is missing"    
        for a_product in range(len(products)):
            return "product already exits"
    

        a_product={"productId":productId,"productName":productName,"productPrice":productPrice}

  
        products.append(a_product)

        return jsonify({"message":f'Product {productName} successfully added'}),200

    def get_products(self):
        if len(products) >1:
            return jsonify({
                "message":"Available Products",
                "Products":products
            }),200
        return jsonify({"message":"No products in inventory"}),404

    def get_a_product(self,productId):
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