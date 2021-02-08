from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

from db import db

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

# https://blog.tecladocode.com/learn-python-advanced-configuration-of-flask-jwt/
# Change the url to the authentication endpoint from /auth to /login
app.config['JWT_AUTH_URL_RULE'] = '/login'
# config JWT to expire within half an hour
from datetime import timedelta
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
# app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
jwt = JWT(app, authenticate, identity)

@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return jsonify({
                'access_token': access_token.decode('utf-8'),
                'user_id': identity.id
            })

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


# https://medium.com/python-features/understanding-if-name-main-in-python-a37a3d4ab0c3
if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True