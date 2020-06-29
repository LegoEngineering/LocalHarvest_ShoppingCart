# app.py or app/__init__.py
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
import json
from bson import ObjectId
from functools import wraps
import jwt
from datetime import datetime, timedelta

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, bytes):
            return o.decode('utf-8')
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)
app.config.from_object('config')

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

app.json_encoder = JSONEncoder

def token_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'Authorization' in request.headers:
            try:
                token = request.headers.get('Authorization').split()[1]
                payload = jwt.decode(token.encode('utf-8'), app.config['SECRET_KEY'], 'HS256')
                request.id = payload['id']
                return f(*args, **kwargs)
            except Exception as e:
                return jsonify({'message': 'Login required'}), 403
        else:
            return jsonify({'message': 'Login required'}), 403
    return wrap

@app.route('/api/hello')
def hello():
    return 'Nice to meet you'

@app.route('/api/changePassword', methods=['POST'])
@token_required
def changePassword():
    users = mongo.db.users
    user = users.find_one({'_id': ObjectId(request.id)})
    if user is None:
        return jsonify({'message': 'Login required'}), 403
    else:
        data = request.get_json()
        password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        users.update_one({'_id': ObjectId(request.id)}, {'$set': {'password': password}}, upsert=False)
        return jsonify({'message': 'Password updated'}), 200

@token_required
def getUser(users):
    user = users.find_one({'_id': ObjectId(request.id)})
    if user is None:
        return jsonify({'message': 'Login required'}), 403
    else:
        user.pop('password', None)
        return jsonify({'value': user}), 200

@app.route('/api/user', methods=['GET', 'POST', 'PATCH'])
def user():
    users = mongo.db.users

    if request.method == 'GET':
        return getUser(users)
    elif request.method == 'POST':
        data = request.get_json()
        user = users.find_one({'username': data['username']})
        if user is None:
            data['password'] = bcrypt.generate_password_hash(data['password']).decode('utf-8')
            result = users.insert_one(data)
            payload = {'id': str(result.inserted_id), 'exp': datetime.utcnow() + timedelta(days=10)}
            token = jwt.encode(payload, app.config['SECRET_KEY'], 'HS256')
            return jsonify({'token': token}), 200
        else:
            return jsonify({'message': 'Account already exists'}), 400

@app.route('/api/login', methods=['POST'])
def login():
    users = mongo.db.users
    data = request.get_json()
    user = users.find_one({"username": data['username']})
    if user is None:
        return jsonify({'message': 'Account does not exist'}), 404
    elif bcrypt.check_password_hash(user['password'], data['password']):
        payload = {'id': str(user['_id']), 'exp': datetime.utcnow() + timedelta(days=10)}
        token = jwt.encode(payload, app.config['SECRET_KEY'], 'HS256')
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Account does not exist'}), 404

@app.route('/api/product', methods=['GET', 'POST', 'PATCH'])
def product():
    products = mongo.db.products
    if request.method == 'GET':
        if products is None:
            return jsonify({'message': 'Product does not exist'}), 200
        if request.args is None:
            allProducts = list(mongo.db.products)
            return jsonify(allProducts), 200
        agr = []
        if 'productname' in request.args:
            prodName = request.args.get('productname')
            prodNameFilter = {'$match': {
                "productname": prodName
            }}
            agr.append(prodNameFilter)
        if 'productweight' in request.args:
            prodWeight = request.args.get('productweight')
            prodWeightFilter = {'$match': {
                "productweight": prodWeight
            }}
            agr.append(prodWeightFilter)
        if 'productprice' in request.args:
            prodPrice = request.args.get('productprice')
            prodPriceFilter = {'$match': {
                "productprice": prodPrice
            }}
            agr.append(prodPriceFilter)
        if 'productsupply' in request.args:
            prodSupply = request.args.get('productsupply')
            prodSupplyFilter = {'$match': {
                "productsupply": prodSupply
            }}
            agr.append(prodSupplyFilter)
        productsFiltered = list(mongo.db.products.aggregate(agr))
        return jsonify(productsFiltered), 200

    elif request.method == 'POST':
        data = request.get_json()
        product = products.find_one({"productname": data['productname']})
        if product is None:
            result = products.insert_one(data)
            return jsonify({'message': 'Product has been added!'}), 200
        else:
            return jsonify({'message': 'Product already exists'}), 400

@app.route('/api/cart', methods=['GET', 'POST', 'PATCH'])
def cart():
    carts = mongo.db.carts
    if request.method == 'GET':
        return jsonify({'message': 'get request'}), 200
    elif request.method == 'POST':
        data = request.get_json()
        result = carts.insert(data)
        hi = list(mongo.db.carts)
        return jsonify(hi), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')