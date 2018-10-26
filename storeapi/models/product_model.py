from flask import jsonify, request
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

        if productName ==" " or not isinstance(productName,str):
            return jsonify({'message':"Product Name cannot be blank or a number"})

        if not isinstance (productPrice,int):
            return jsonify({'message':"Price can only be digits"})

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