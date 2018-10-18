from storeapi.views import app
from storeapi.models import Product, products
import unittest

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()
        self.request_data={
            "productId":1,
            "productName":"Foam",
            "productPrice":3000
        }
        self.sale_data={
            "saleId":'1',
            "productName":"Foam",
            "created_by":"myself",
            "details":"Mattress material"
        }
     
if __name__ == "__main__":
    unittest.main()