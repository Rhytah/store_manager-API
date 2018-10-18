
from app import create_app
from storeapi.views import app

app = create_app('development')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
