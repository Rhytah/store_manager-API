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
        # self.assertIn(
        #     'Product Foam successfully added', str(response.data)
        # )
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
                            headers={'Authorization':
                                        'Bearer {}'.format(self.token)})
      
        self.assertEqual(response.status_code, 200)
    
    def test_fetch_products(self):
        response = self.test_client.get( 
            '/api/v1/products', data=json.dumps(self.sale_data), content_type = 'application/json')
        self.assertEqual(response.status_code,200)
    
    def test_fetch_single_product(self):
        response=self.test_client.post(
            'api/v1/products', data=json.dumps(self.request_data), content_type = 'application/json')
        response = self.test_client.get(
            '/api/v1/products/1',  content_type='application/json')
        self.assertEqual(response.status_code,200)
        


    def test_add_sale_order(self):
        with self.app.app_context():
            token = create_access_token('attendant')
            headers = {'Authorization': f'Bearer {token}'}
            response = self.test_client.post(
                '/api/v1/sales',
                headers=headers,
                content_type='application/json'
            )
            return(response.status)
        self.assertEqual(response.status_code,200)
        self.assertIn(
            'You have successfully created a sale order', str(response.data)
        )
    def test_fetch_single_sale_order(self):
        with self.app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization': f'Bearer {token}'}
            response = self.test_client.get(
                '/api/v1/sales/1',
                headers=headers,
                content_type='application/json'
            )
            return(response.status)
        self.assertEqual(200, response.status_code)
       
        self.assertEqual(response.status_code,200)

    def test_fetch_all_sale_orders(self):
        
        with self.app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization': f'Bearer {token}'}
            response = self.test_client.get(
                '/api/v1/sales',
                headers=headers,
                content_type='application/json'
            )
            return(response.status)
        self.assertEqual(200, response.status_code)