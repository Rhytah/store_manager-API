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
        
    def test_fetch_single_sale_order(self):
        with self.app.app_context():
            token = create_access_token('attendant')
            headers = {'Authorization': f'Bearer {token}'}
            response = self.test_client.get(
                '/api/v1/sales/1',
                headers=headers,
                content_type='application/json'
            )
            return(response.status)

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
