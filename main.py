from config import app
from flask import request
from utils import *

@app.route('/users/', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return app.response_class(response = json.dumps(get_all_users()), status=200)
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_user(request.json)
        elif isinstance(request.json, dict):
            insert_data_user([request.json])
        else:
            print('Непонятный тип данных')
        return app.response_class(response = json.dumps(request.json), status=200)

@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_users_by_id(user_id):
    if request.method == 'GET':
        data = get_all_users()
        for row in data:
            if row.get('id') == user_id:
                return app.response_class(response = json.dumps(row), status=200)
    elif request.method == 'PUT':
        update_user(User, user_id, request.json)
        return app.response_class(response=json.dumps(['OK']), status=200)
    elif request.method == 'DELETE':
        universal_delete(User, user_id)
        return app.response_class(response=json.dumps(['OK']), status=200)


@app.route('/orders/', methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        return app.response_class(response = json.dumps(get_all_orders()), status=200)
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_order(request.json)
        elif isinstance(request.json, dict):
            insert_data_order([request.json])
        else:
            print('Непонятный тип данных')
        return app.response_class(response = json.dumps(request.json), status=200)

@app.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def get_orders_by_id(order_id):
    if request.method == 'GET':
        data = get_all_orders()
        for row in data:
            if row.get('id') ==order_id:
                return app.response_class(response = json.dumps(row), status=200)
    elif request.method == 'PUT':
        update_order(Order, order_id, request.json)
        return app.response_class(response=json.dumps(['OK']), status=200)
    elif request.method == 'DELETE':
        universal_delete(Order, order_id)
        return app.response_class(response=json.dumps(['OK']), status=200)


@app.route('/offers/', methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        return app.response_class(response = json.dumps(get_all_offers()), status=200)
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_offer(request.json)
        elif isinstance(request.json, dict):
            insert_data_offer([request.json])
        else:
            print('Непонятный тип данных')
        return app.response_class(response = json.dumps(request.json), status=200)

@app.route('/offers/<int:offer_id>', methods=['GET', 'PUT', 'DELETE'])
def get_offers_by_id(offer_id):
    if request.method == 'GET':
        data = get_all_offers()
        for row in data:
            if row.get('id') == offer_id:
                return app.response_class(response = json.dumps(row), status=200)
    elif request.method == 'PUT':
        update_offer(Offer, offer_id, request.json)
        return app.response_class(response=json.dumps(['OK']), status=200)
    elif request.method == 'DELETE':
        universal_delete(Offer, offer_id)
        return app.response_class(response=json.dumps(['OK']), status=200)

if __name__ == '__main__':
    init_db()
    app.run()