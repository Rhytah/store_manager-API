from tests import BaseTestCase
import json
from flask import jsonify
from flask_jwt_extended import JWTManager, create_access_token

class RequestTestCase(BaseTestCase):


    def test_add_product_without_token(self):
        response = self.test_client.post(
            '/api/v1/products', data=json.dumps(self.request_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,401)
        self.assertIn(
            'Missing Authorization Header', str(response.data)
        )
    def test_add_product_as_attendant(self):
        with self.app.app_context():
            token = create_access_token('attendant')
            headers = {'Authorization': f'Bearer {token}'}
            response = self.test_client.post(
                '/api/v1/product',
                headers=headers,
                content_type='application/json'
            )
            return(response.status)
        self.assertEqual(response.status_code,401)
        self.assertIn(
            'Access denied, Log in as admin to add Products', str(response.data)
        )
    def test_admin_can_add_product(self): 
        response = self.test_client.post('/api/v1/login',
                                    data=json.dumps(self.auth_data),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', str(response.data))
        
        login_response = response.json
        self.token = login_response['access_token']
        response = self.test_client.post('/api/v1/products',
                            data=json.dumps(self.request_data),
                            content_type='application/json',
                            headers={'Authorization':f'Bearer {self.token}'}
                            )
        self.assertEqual(response.status_code, 200)
    
    def test_fetch_products(self):
        response = self.test_client.post('/api/v1/login',
                                    data=json.dumps(self.auth_data),
                                    content_type='application/json'
                                    )
        # self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', str(response.data))
        
        login_response = response.json
        self.token = login_response['access_token']
        response = self.test_client.post('/api/v1/products',
                            data=json.dumps(self.request_data),
                            content_type='application/json',
                            headers={'Authorization':
                                        'Bearer {}'.format(self.token)})
      
        self.assertEqual(response.status_code, 200)
        response = self.test_client.get( 
            '/api/v1/products', data=json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code,200)
        self.assertIn("Available Products", str(response.data))
    
    def test_fetch_single_product(self):
        response=self.test_client.post(
            'api/v1/products', data=json.dumps(self.request_data), content_type = 'application/json')
        response = self.test_client.get(
            '/api/v1/products/1',  content_type='application/json')
        self.assertEqual(response.status_code,200)
        
