from flask import Flask
# from storeapi.views import blueprint
# from . import views

app = Flask(__name__)
# app.register_blueprint(blueprint, url_prefix='/api/v1')

from storeapi.views import auth_views, product_views,sale_views



