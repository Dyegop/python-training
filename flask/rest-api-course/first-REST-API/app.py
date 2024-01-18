from flask import Flask, jsonify, request, render_template


app = Flask(__name__)


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



# Home
@app.route('/')
def home():
    return render_template("index.html")


# GET /stores - return all the stores
@app.route('/stores')
def get_stores():
    # jsonify - method to convert a variable into json
    # Use always double quotes in jsons
    return jsonify({'stores': stores})


# GET /store <string:name> - return a given store
# By default, any endpoint does a GET
# This <string:name> is Flask syntax to pass arguments to an endpoint
# The argument must match with the parameter in the method (in this case, "name")
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over stores
    # If store name matches, return it
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GET /store <string:name>/items - return all items in a store
@app.route('/store/<string:name>/items')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


# GET /store <string:name>/items - return all items in a store
@app.route('/store/<string:name>/<string:item_name>')
def get_item_in_store(name, item_name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'item': [item for item in store['items'] if item['name'] == item_name]})
    return jsonify({'message': 'store not found'})


# POST /store data: {name:}
# "methods" allow us to define an HTTP method
@app.route('/store', methods=['POST'])
def create_store():
    # Get data coming back from our request
    # Browser will send data (the name of the store in this case) and we will be able to access it
    # Data is sent in the body of the request
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# POST /store <string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


# A port is an area in the computer where the app will recieve requests and return responses
app.run(port=5000, debug=True)
