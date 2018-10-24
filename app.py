# from storeapi.views.auth_views import app
# from storeapi.views.product_views import app
# from storeapi.views.sale_views import app
from storeapi import app
from flask import Flask
from config import app_configuration
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)

jwt = JWTManager(app)

def create_app(mode):
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config.from_object(app_configuration[mode])
    # app.config['JWT_SECRET_KEY'] = 'andela13' 
    

       
    return app
if __name__=='__main__':
    app.run(debug=True)
