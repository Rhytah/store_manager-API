from tests import BaseTestCase
import json
from flask import jsonify

class RequestTestCase(BaseTestCase):

    def test_add_product(self):
        response = self.test_client.post(
            '/api/v1/admin/products', data=json.dumps(self.request_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,200)
        self.assertIn(
            'Product Foam successfully added', str(response.data)
        )
    def test_add_product_nonadmin(self):
        response = self.test_client.post(
        '/api/v1/products', data=json.dumps(self.request_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,405)
        
    def test_fetch_products(self):
        response = self.test_client.get( 
            '/api/v1/products', data=json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code,200)
    
    def test_fetch_single_product(self):
        response=self.test_client.post(
            'api/va/admin/products', data=json.dumps(self.request_data), content_type = 'application/json')
        response = self.test_client.get(
            '/api/v1/products/1',  content_type='application/json')
        self.assertEqual(response.status_code,200)
        


    def test_add_sale_order(self):    
        response = self.test_client.post(
            '/api/v1/attendant/sales', data=json.dumps(self.sale_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,200)
        self.assertIn(
            'You have successfully created a sale order', str(response.data)
        )
    def test_fetch_single_sale_order(self):
        response = self.test_client.get(
            '/api/v1/sales/1', data=json.dumps(self.sale_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,200)

    def test_fetch_all_sale_orders(self):
        response = self.test_client.get( 
            '/api/v1/admin/sales', data=json.dumps(self.sale_data), content_type = 'application/json')
        self.assertEqual(response.status_code,200)
    
    def test_index(self):
        response = self.test_client.get(
            '/'
        )
        self.assertEqual(response.status_code,200)
