from flask import Flask, request
from flask_restful import Resource, Api



# Create our Flask application
app = Flask(__name__)

# Create our API application
api = Api(app)

# Data
stores = ['My Evil Store']



class Store(Resource):
    def get(self, name):
        store = next(filter(lambda x: x == name, stores), None)
        return store, 200 if store else 404

    def post(self, name):
        request_data = request.get_json()
        new_store = request_data["name"]
        stores.append(new_store)
        return new_store, 200

    def put(self, name):
        request_data = request.get_json()
        new_store = request_data["name"]
        stores.append(new_store)
        return new_store, 200



class StoreList(Resource):
    def get(self):
        return stores, 200




api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')



app.run(port=5000, debug=True)
