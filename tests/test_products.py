from tests import BaseTestCase
from flask import jsonify,json,Flask
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
        self.assertIn(
            'Access denied, Log in as admin to add Products', str(response.data)
        )
    def test_admin_can_add_product(self): 
        with self.app.app_context():
            token = create_access_token('admin')
            headers={'Authorization':f'Bearer {token}'}

            response = self.test_client.post(
                '/api/v1/products',
                headers=headers,
                content_type='application/json')
            return(response.status)
        self.assertIn("Product Foam successfully added", str (response.data))
    
    def test_fetch_products(self):
        response = self.test_client.get( 
            '/api/v1/products', data=json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code,404)
        self.assertIn("No products in inventory", str(response.data))

        with self.app.app_context():
            token = create_access_token('admin')
            headers={'Authorization':f'Bearer {token}'}

            response = self.test_client.post(
                '/api/v1/products',
                headers=headers,
                content_type='application/json')
            return(response.status)        
        response = self.test_client.post('/api/v1/products',
                            content_type='application/json',
                            data=json.dumps(self.request_data)
                            )      
        self.assertEqual(response.status_code, 200)
        self.assertIn("Available products",str(response.data))

    def test_fetch_single_product_emptylist(self):
        response = self.test_client.get(
            '/api/v1/products/1', data=json.dumps(self.request_data), content_type='application/json')
        self.assertEqual(response.status_code,404)
        self.assertIn(  "No products in inventory", str(response.data))
        
    def test_fetch_single_product(self):    
        with self.app.app_context():
            token = create_access_token('admin')
            headers={'Authorization':f'Bearer {token}'}

            response = self.test_client.post(
                '/api/v1/products',
                headers=headers,
                content_type='application/json')
            return(response.status)        
        response = self.test_client.post('/api/v1/products/1',
                            content_type='application/json',
                            data=json.dumps(self.request_data)
                            )      
        self.assertEqual(response.status_code, 200)
        self.assertIn("You have fetched product",str(response.data))