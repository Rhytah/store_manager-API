from storeapi import app
import json
from storeapi.models.product_model import Product, products
import unittest

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()
        self.app = app
        self.app.config['TESTING'] = True
        self.token=''
        self.auth_data = {
            'username': 'admin',
            'password': 'pass'
        }
        self.auth_data2 ={
            'username':'',
            'password':''
        }
        self.auth_data3={
            "username":'admin',
            "password":'password'
        }
        self.auth_data_attendant ={
            "username":"attendant",
            "password":"password"
        }
        self.request_data={
            "productId":1,
            "productName":"Foam",
            "productPrice":3000
        }
        self.sale_data={
            "saleId":1,
            "productName":"Foam",
            "cost":5000,
            "quantity":4,
            "created_by":"attendant",
            "details":"Mattress material",
            "total":20000
        }
        self.sample_sales =[
            {
            "saleId":1,
            "productName":"Foam",
            "cost":5000,
            "quantity":4,
            "created_by":"attendant",
            "details":"Mattress material",
            "total":20000
            }
            ]
if __name__ == "__main__":
    unittest.main()