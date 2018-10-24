from flask import Flask,json

from tests import BaseTestCase
from flask_jwt_extended import JWTManager, create_access_token


class AuthTestCase(BaseTestCase):

    def test_index(self):
        response= self.test_client.get('/', content_type='application/json')
        # self.assertEqual(response.status_code,200)
        self.assertIn("StoreManager App. Manage your Products and Sales efficiently",str(response.data))

    def test_admin_login(self):
        response = self.test_client.post('/api/v1/login',
                                    data=json.dumps(self.auth_data),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertIn("logged in as admin",  str(response.data))
    
    def test_attendant_login(self):
        response = self.test_client.post('/api/v1/login',
                                    data=json.dumps(self.auth_data_attendant),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("logged in as attendant", str(response.data))

    def test_user_login_without_username_and_password(self):
        response = self.test_client.post('/api/v1/login',
                                    data=json.dumps(self.auth_data2),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code,401)
        self.assertIn('enter your credentials',str(response.data))

    def test_user_login_with_wrong_password(self):
        response = self.test_client.post('/api/v1/login',
                                    data=json.dumps(self.auth_data3),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code,401)
        self.assertIn('Invalid username/password',str(response.data))
