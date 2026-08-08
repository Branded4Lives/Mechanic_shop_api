from flask import jsonify, request

from app.extensions import db
from app.models import Mechanic

from . import mechanics_bp
from .schemas import (
    mechanic_create_schema,
    mechanic_schema,
    mechanic_update_schema,
    mechanics_schema,
)


def get_mechanic_or_404(mechanic_id):
    mechanic = db.session.get(Mechanic, mechanic_id)

    if not mechanic:
        return None, (jsonify({"error": "Mechanic not found"}), 404)

    return mechanic, None


@mechanics_bp.post("/")
def create_mechanic():
    data = mechanic_create_schema.load(request.get_json() or {})

    existing_mechanic = Mechanic.query.filter_by(email=data["email"]).first()
    if existing_mechanic:
        return jsonify({"error": "A mechanic with that email already exists"}), 409

    mechanic = Mechanic(**data)
    db.session.add(mechanic)
    db.session.commit()

    return jsonify(mechanic_schema.dump(mechanic)), 201


@mechanics_bp.get("/")
def get_mechanics():
    mechanics = Mechanic.query.order_by(Mechanic.id).all()
    return jsonify(mechanics_schema.dump(mechanics)), 200


@mechanics_bp.get("/<int:mechanic_id>")
def get_mechanic(mechanic_id):
    mechanic, error = get_mechanic_or_404(mechanic_id)
    if error:
        return error

    return jsonify(mechanic_schema.dump(mechanic)), 200


@mechanics_bp.put("/<int:mechanic_id>")
def update_mechanic(mechanic_id):
    mechanic, error = get_mechanic_or_404(mechanic_id)
    if error:
        return error

    data = mechanic_update_schema.load(request.get_json() or {})

    if "email" in data and data["email"] != mechanic.email:
        existing_mechanic = Mechanic.query.filter_by(email=data["email"]).first()
        if existing_mechanic:
            return jsonify({"error": "A mechanic with that email already exists"}), 409

    for key, value in data.items():
        setattr(mechanic, key, value)

    db.session.commit()
    return jsonify(mechanic_schema.dump(mechanic)), 200


@mechanics_bp.delete("/<int:mechanic_id>")
def delete_mechanic(mechanic_id):
    mechanic, error = get_mechanic_or_404(mechanic_id)
    if error:
        return error

    db.session.delete(mechanic)
    db.session.commit()

    return jsonify({"message": "Mechanic deleted successfully"}), 200
