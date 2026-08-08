from marshmallow import Schema, fields, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app.models import Customer


class CustomerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        include_fk = True
        load_instance = False


class CustomerCreateSchema(Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=1))
    last_name = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    phone = fields.String(load_default=None)
    address = fields.String(load_default=None)


class CustomerUpdateSchema(Schema):
    first_name = fields.String(validate=validate.Length(min=1))
    last_name = fields.String(validate=validate.Length(min=1))
    email = fields.Email()
    phone = fields.String(allow_none=True)
    address = fields.String(allow_none=True)


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
customer_create_schema = CustomerCreateSchema()
customer_update_schema = CustomerUpdateSchema()
