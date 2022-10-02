"""
FLASK-RESTFUL
-Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs.
-It is a lightweight abstraction that works with your existing ORM/libraries.
-Flask-RESTful encourages best practices with minimal setup.

API AUTHENTICATION WITH FLASK-JWT
-How API Authentication works
    -The user writes its username and password on your website.
    -The username and password gets sent to the backend API.
    -The API looks for any record on the User table that matches with both parameters (username and password).
    -If a user is found, it generates a token for that user and responds status_code=200 back to the front end.
    -The front-end will use that token from now on to make any future request.

-Ways of create tokens:
    -Basic Token	- Example: ecff2099b95ed507a27a4717ec78965d529cc346
    -Bearer Token	- Example: YWxlc2FuY2hlenI6NzE0YmZhNDNlN2MzMTJiZTk5OWQwYWZlYTg5MTQ4ZTc=
    -JWT Token	    - Example: eyJhbGciOiJIUzI1NiIsInR5c.eyJzdWIiOFt2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpM

-JSON Web Token or JWT is an open standard to create tokens and it is basically an obfuscation of data.
-JSON Web Token includes a structure, which can be decrypted by the server that allows you to  authenticate the
identity of the user of that application.
-Flask-JWT is an extension for Flask to manage JWT authenticaton.
-For additional information, see https://content.breatheco.de/en/lesson/what-is-JWT-and-how-to-implement-with-Flask
"""

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
import security




# Create our Flask application
app = Flask(__name__)

# Add our secret key for authentication
app.secret_key = 'diego03'

# Create our API application
api = Api(app)

# Create authenticate object
# JWT creates a new endpoint `/auth`, then it gets a username and a password and send it to the authentication_handler
# The `/auth` endpoint returns a token that it sends to the identity function
jwt = JWT(app=app, authentication_handler=security.authenticate, identity_handler=security.identity)


# Data
stores = [
    {
        'name': 'My Evil Store',
        'items': [
            {
                'name': 'broken mirror',
                'price': 15.99
            },
            {
                'name': 'monkey paw',
                'price': 99.99
            },
            {
                'name': 'black hat',
                'price': 29.99
            }
        ]
    },
    {
        'name': 'My Good Store',
        'items': [
            {
                'name': 'silver mirror',
                'price': 25.99
            },
            {
                'name': 'rabbit foot',
                'price': 109.99
            },
            {
                'name': 'white hat',
                'price': 39.99
            }
        ]
    },
]


items = []


# API Resources
# Every resource of the API has to be a class that inherits from Resource
class Store(Resource):
    # jwt_required is a decorator that enforces an HTTP request to authenticate the user
    @jwt_required()
    # The name of the method must be the type of request we want to send
    def get(self, name):
        """ Return a store """
        # next() - return next item or None if there are no items left
        # This expression returns next item in stores that evaluates lambda function to True
        store = next(filter(lambda x: x['name'] == name, stores), None)
        # We don't need to use jsonify return value since flask_restful already does it
        # Therefore, we can return dict objects
        return {'store': store}, 200 if store else 404

    def post(self, name):
        """ Creates a store """
        if next(filter(lambda x: x['name'] == name, stores), None) is not None:
            return {'message': f'A store with name {name} already exists'}, 400

        # If we use data from the request, a content-type parameter will be required
        request_data = request.get_json()
        new_store = {'name': name, 'items': request_data["items"]}
        stores.append(new_store)
        return new_store, 200




class Items(Resource):
    #@jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': f'An item with name {name} already exists'}, 400
        request_data = request.get_json(silent=True)
        item = {'name': name, 'price': request_data['price']}
        items.append(item)
        return item, 201

    def put(self, name):
        # Create a parser for the request
        parser = reqparse.RequestParser()
        # Add argument
        # When we run the request, this will look at the payloads and parse the arguments
        # If we add arguments in the JSON payload (the json sent in the request) that are not parsed,
        # they will be skipped
        parser.add_argument(
            'price',
            type=float,
            required=True,
            help="This field cannot be left blank!"
        )
        data = parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {"message": "Item deleted"}




class ItemList(Resource):
    def get(self):
        return {'items': items}, 200





# Add API-Rest resource
api.add_resource(Items, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')

app.run(port=5000, debug=True)
