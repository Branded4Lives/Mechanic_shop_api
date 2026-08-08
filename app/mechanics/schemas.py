from marshmallow import Schema, fields, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app.models import Mechanic


class MechanicSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Mechanic
        include_fk = True
        load_instance = False


class MechanicCreateSchema(Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=1))
    last_name = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    phone = fields.String(load_default=None)
    specialty = fields.String(load_default=None)


class MechanicUpdateSchema(Schema):
    first_name = fields.String(validate=validate.Length(min=1))
    last_name = fields.String(validate=validate.Length(min=1))
    email = fields.Email()
    phone = fields.String(allow_none=True)
    specialty = fields.String(allow_none=True)


mechanic_schema = MechanicSchema()
mechanics_schema = MechanicSchema(many=True)
mechanic_create_schema = MechanicCreateSchema()
mechanic_update_schema = MechanicUpdateSchema()
