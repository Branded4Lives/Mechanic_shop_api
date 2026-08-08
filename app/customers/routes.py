from flask import jsonify, request

from app.extensions import db
from app.models import Customer

from . import customers_bp
from .schemas import (
    customer_create_schema,
    customer_schema,
    customer_update_schema,
    customers_schema,
)


def get_customer_or_404(customer_id):
    customer = db.session.get(Customer, customer_id)

    if not customer:
        return None, (jsonify({"error": "Customer not found"}), 404)

    return customer, None


@customers_bp.post("/")
def create_customer():
    data = customer_create_schema.load(request.get_json() or {})

    existing_customer = Customer.query.filter_by(email=data["email"]).first()
    if existing_customer:
        return jsonify({"error": "A customer with that email already exists"}), 409

    customer = Customer(**data)
    db.session.add(customer)
    db.session.commit()

    return jsonify(customer_schema.dump(customer)), 201


@customers_bp.get("/")
def get_customers():
    customers = Customer.query.order_by(Customer.id).all()
    return jsonify(customers_schema.dump(customers)), 200


@customers_bp.get("/<int:customer_id>")
def get_customer(customer_id):
    customer, error = get_customer_or_404(customer_id)
    if error:
        return error

    return jsonify(customer_schema.dump(customer)), 200


@customers_bp.put("/<int:customer_id>")
def update_customer(customer_id):
    customer, error = get_customer_or_404(customer_id)
    if error:
        return error

    data = customer_update_schema.load(request.get_json() or {})

    if "email" in data and data["email"] != customer.email:
        existing_customer = Customer.query.filter_by(email=data["email"]).first()
        if existing_customer:
            return jsonify({"error": "A customer with that email already exists"}), 409

    for key, value in data.items():
        setattr(customer, key, value)

    db.session.commit()
    return jsonify(customer_schema.dump(customer)), 200


@customers_bp.delete("/<int:customer_id>")
def delete_customer(customer_id):
    customer, error = get_customer_or_404(customer_id)
    if error:
        return error

    db.session.delete(customer)
    db.session.commit()

    return jsonify({"message": "Customer deleted successfully"}), 200
