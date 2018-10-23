class User:
    def __init__(self,userId,username,password,role):
        self.userId=userId
        self.username=username
        self.password=password
        self.role=bool(role)
        

class Product:
    def ___init__(self, productId,productName,productPrice):
        self.productId=productId
        self.productName=productName
        self.productPrice=productPrice
products=[]
a_product={}

class Sale:
    def __init__(self, saleId,productName,created_by, details):
        self.saleId=saleId
        self.productName=productName
        self.created_by=created_by
        self.details=details
sale_orders=[]
a_sale_order={}