products=[]
a_product={}
sale_orders=[]
a_sale_order={}

class User:
    def __init__(self, name,role):
        self.name=name
        self.role=role

class Product:
    def ___init__(self, productId,productName,productPrice):
        self.productId=productId
        self.productName=productName
        self.productPrice=productPrice

class Sale:
    def __init__(self, saleId,productName,created_by, details):
        self.saleId=saleId
        self.productName=productName
        self.created_by=created_by
        self.details=details
