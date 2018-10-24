from flask import Flask


app = Flask(__name__)


from storeapi.views import auth_views, product_views,sale_views



