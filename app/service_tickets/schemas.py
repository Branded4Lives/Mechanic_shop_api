from marshmallow import Schema, fields, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app.customers.schemas import CustomerSchema
from app.mechanics.schemas import MechanicSchema
from app.models import ServiceTicket


class ServiceTicketSchema(SQLAlchemyAutoSchema):
    customer = fields.Nested(
        CustomerSchema(only=("id", "first_name", "last_name", "email"))
    )
    mechanics = fields.List(
        fields.Nested(
            MechanicSchema(only=("id", "first_name", "last_name", "email", "specialty"))
        )
    )

    class Meta:
        model = ServiceTicket
        include_fk = True
        load_instance = False


class ServiceTicketCreateSchema(Schema):
    customer_id = fields.Integer(required=True)
    vin = fields.String(required=True, validate=validate.Length(min=1, max=17))
    description = fields.String(required=True, validate=validate.Length(min=1))
    service_date = fields.String(load_default=None)
    status = fields.String(load_default="open")
    mechanic_ids = fields.List(fields.Integer(), load_default=list)


class ServiceTicketUpdateSchema(Schema):
    customer_id = fields.Integer()
    vin = fields.String(validate=validate.Length(min=1, max=17))
    description = fields.String(validate=validate.Length(min=1))
    service_date = fields.String(allow_none=True)
    status = fields.String()


service_ticket_schema = ServiceTicketSchema()
service_tickets_schema = ServiceTicketSchema(many=True)
service_ticket_create_schema = ServiceTicketCreateSchema()
service_ticket_update_schema = ServiceTicketUpdateSchema()
