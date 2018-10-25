from storeapi import app
from storeapi.views import auth_views,sale_views,product_views
from flask import Flask
from config import app_configuration
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)

jwt = JWTManager(app)

def create_app(mode):
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config.from_object(app_configuration[mode])
     
    
    return app
if __name__=='__main__':
    app.run(debug=True, port=5000)

