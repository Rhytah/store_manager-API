from flask import jsonify, request


class Sale:
    def __init__(self,**kwargs):
        # self.saleId=args[0]
        # self.productName=args[1]
        # self.created_by=args[2]
        # self.details=args[3]
        self.sale_orders=[]

        
# add a sale order
    def add_sale(self,*sale_data):
        sale_data=request.get_json()
        saleId=len(self.sale_orders)+1
        productName=sale_data.get('productName')
        created_by=sale_data.get('created_by')
        details =sale_data.get('details')

        a_sale_order={'saleId':saleId, 'productName':productName, 'created_by':created_by,'details':details}
        if a_sale_order in self.sale_orders:
            return jsonify({"Alert":"Sale order already exists"})
        self.sale_orders.append(a_sale_order)
        
        return jsonify({"message":f"{created_by}You have successfully created a sale order for {productName}"}),401


# get all sale order
    def get_sales(self):
        if len(self.sale_orders) <1:
            return jsonify ({
                "message":"No sale orders at the moment"
            }),404

        if len(self.sale_orders) >1:
            return jsonify({
                "message":"Sale orders",
                "Sales":self.sale_orders
            }),200

# get a specific sale order
    def fetch_sale(self,saleId):
        if len(self.sale_orders)<1:
            return jsonify({
                "message":"NO sale orders at the moment"
            }),404  
        
        if len(self.sale_orders)>1:
            for a_sale_order in self.sale_orders:
                if a_sale_order['saleId']==saleId:
                    return jsonify({
                        "message":"You have fetched a sale order",
                        "Sale_order":a_sale_order
                    }),200      
        