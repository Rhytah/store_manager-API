from flask import Flask
# from app import create_app
from storeapi import app

# app = create_app('development')
app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
