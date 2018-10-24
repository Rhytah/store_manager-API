from flask import Flask,json

from tests import BaseTestCase
from flask_jwt_extended import JWTManager, create_access_token


class SalesTestCase(BaseTestCase):

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
            'myselfYou have successfully created a sale order', str(response.data)
        )
    def test_fetch_single_sale_order(self):
        # with self.app.app_context():
        #     token = create_access_token('admin')
        #     headers = {'Authorization': f'Bearer {token}'}
        #     response = self.test_client.get(
        #         '/api/v1/sales/1',
        #         headers=headers,
        #         content_type='application/json'
        #     )
        #     return(response.status)
        response= self.test_client.get(
            '/api/v1/sales/1',
            data=json.dumps(self.sale_data),
            content_type='application/json'
        )
              
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
        # self.assertEqual(200, response.status_code)
