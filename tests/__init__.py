from storeapi.views import app
import json
from storeapi.models import Product, products
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

    def test_user_login(self):
        
        response = self.test_client.post('/api/v1/login',
                                    data=json.dumps(self.auth_data),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', str(response.data))
     
if __name__ == "__main__":
    unittest.main()