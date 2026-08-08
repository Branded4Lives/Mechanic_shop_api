from flask import jsonify, request

from app.extensions import db
from app.models import Customer, Mechanic, ServiceTicket

from . import service_tickets_bp
from .schemas import (
    service_ticket_create_schema,
    service_ticket_schema,
    service_ticket_update_schema,
    service_tickets_schema,
)


def get_ticket_or_404(ticket_id):
    ticket = db.session.get(ServiceTicket, ticket_id)

    if not ticket:
        return None, (jsonify({"error": "Service ticket not found"}), 404)

    return ticket, None


def get_mechanic_or_404(mechanic_id):
    mechanic = db.session.get(Mechanic, mechanic_id)

    if not mechanic:
        return None, (jsonify({"error": "Mechanic not found"}), 404)

    return mechanic, None


@service_tickets_bp.post("/")
def create_service_ticket():
    data = service_ticket_create_schema.load(request.get_json() or {})

    customer = db.session.get(Customer, data["customer_id"])
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    mechanic_ids = data.pop("mechanic_ids", [])
    mechanics = []

    for mechanic_id in mechanic_ids:
        mechanic = db.session.get(Mechanic, mechanic_id)
        if not mechanic:
            return jsonify({"error": f"Mechanic {mechanic_id} not found"}), 404
        mechanics.append(mechanic)

    ticket = ServiceTicket(**data)
    ticket.mechanics.extend(mechanics)

    db.session.add(ticket)
    db.session.commit()

    return jsonify(service_ticket_schema.dump(ticket)), 201


@service_tickets_bp.get("/")
def get_service_tickets():
    tickets = ServiceTicket.query.order_by(ServiceTicket.id).all()
    return jsonify(service_tickets_schema.dump(tickets)), 200


@service_tickets_bp.get("/<int:ticket_id>")
def get_service_ticket(ticket_id):
    ticket, error = get_ticket_or_404(ticket_id)
    if error:
        return error

    return jsonify(service_ticket_schema.dump(ticket)), 200


@service_tickets_bp.put("/<int:ticket_id>")
def update_service_ticket(ticket_id):
    ticket, error = get_ticket_or_404(ticket_id)
    if error:
        return error

    data = service_ticket_update_schema.load(request.get_json() or {})

    if "customer_id" in data:
        customer = db.session.get(Customer, data["customer_id"])
        if not customer:
            return jsonify({"error": "Customer not found"}), 404

    for key, value in data.items():
        setattr(ticket, key, value)

    db.session.commit()
    return jsonify(service_ticket_schema.dump(ticket)), 200


@service_tickets_bp.put("/<int:ticket_id>/assign-mechanic/<int:mechanic_id>")
def assign_mechanic(ticket_id, mechanic_id):
    ticket, ticket_error = get_ticket_or_404(ticket_id)
    if ticket_error:
        return ticket_error

    mechanic, mechanic_error = get_mechanic_or_404(mechanic_id)
    if mechanic_error:
        return mechanic_error

    if mechanic not in ticket.mechanics:
        ticket.mechanics.append(mechanic)

    db.session.commit()
    return jsonify(service_ticket_schema.dump(ticket)), 200


@service_tickets_bp.put("/<int:ticket_id>/remove-mechanic/<int:mechanic_id>")
def remove_mechanic(ticket_id, mechanic_id):
    ticket, ticket_error = get_ticket_or_404(ticket_id)
    if ticket_error:
        return ticket_error

    mechanic, mechanic_error = get_mechanic_or_404(mechanic_id)
    if mechanic_error:
        return mechanic_error

    if mechanic not in ticket.mechanics:
        return jsonify({"error": "Mechanic is not assigned to this ticket"}), 400

    ticket.mechanics.remove(mechanic)
    db.session.commit()

    return jsonify(service_ticket_schema.dump(ticket)), 200


@service_tickets_bp.delete("/<int:ticket_id>")
def delete_service_ticket(ticket_id):
    ticket, error = get_ticket_or_404(ticket_id)
    if error:
        return error

    db.session.delete(ticket)
    db.session.commit()

    return jsonify({"message": "Service ticket deleted successfully"}), 200
