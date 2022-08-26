from models import *
from config import db
import json

def insert_data_user(input_data):
    for row in input_data:
        db.session.add(
            User(
                id=row.get("id"),
                first_name=row.get("first_name"),
                last_name=row.get("last_name"),
                age=row.get("age"),
                email=row.get("email"),
                role=row.get("role"),
                phone=row.get("phone")
            )
        )
    db.session.commit()

def insert_data_order(input_data):
    for row in input_data:
        db.session.add(
            Order(
                id=row.get("id"),
                name=row.get("name"),
                description=row.get("description"),
                start_date=row.get("start_date"),
                end_date=row.get("end_date"),
                address=row.get("address"),
                price=row.get("price"),
                customer_id=row.get("customer_id"),
                executor_id=row.get("executor_id")
            )
        )
    db.session.commit()

def insert_data_offer(input_data):
    for row in input_data:
        db.session.add(
            Offer(
                id=row.get("id"),
                order_id=row.get("order_id"),
                executor_id=row.get("executor_id")
            )
        )
    db.session.commit()

db.drop_all()
db.create_all()

def get_all_users():
    result = []
    for row in User.query.all():
        result.append(row.to_dict())
    return result

def get_all_orders():
    result = []
    for row in Order.query.all():
        result.append(row.to_dict())
    return result

def get_all_offers():
    result = []
    for row in Offer.query.all():
        result.append(row.to_dict())
    return result

def update_user(model, user_id, values):
    data = db.session.query(model).get(user_id)
    data.first_name = values.get('first_name')
    data.last_name = values.get('last_name')
    data.age = values.get('age')
    data.email = values.get('email')
    data.role = values.get('role')
    data.phone = values.get('phone')
    db.session.commit()


def update_order(model, order_id, values):
    data = db.session.query(model).get(order_id)
    data.name = values.get('name')
    data.description = values.get('description')
    data.start_date = values.get('start_date')
    data.end_date = values.get('end_date')
    data.address = values.get('address')
    data.price = values.get('price')
    data.customer_id = values.get('customer_id')
    data.executor_id = values.get('executor_id')
    db.session.commit()

def update_offer(model, offer_id, values):
    data = db.session.query(model).get(offer_id)
    data.order_id = values.get('order_id')
    data.executor_id = values.get('executor_id')
    db.session.commit()

def universal_delete(model, user_id):
    db.session.query(model).filter(model.id == user_id).delete()
    db.session.commit()

def init_db():
    with open('data/user.json') as file:
        insert_data_user(json.load(file))
    with open('data/order.json') as file:
        insert_data_order(json.load(file))
    with open('data/offer.json') as file:
        insert_data_offer(json.load(file))
