from marshmallow import Schema, ValidationError, fields, validate, validates
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models import Project
from app.api.validators.architecture_validation_schema import ArchitectureValidateSchema
from shared.factories import db
from app.api.validators.resize_validate_schema import ResizeValidateSchema


class ProjectValidateSchema(Schema):
    name = fields.String(required=True)
    tag = fields.String(required=True)
    description = fields.String(required=False, default="")
    dataset = fields.String(required=True)
    api_key = fields.String(required=True)
    tags = fields.List(fields.String(), required=False)
    classes = fields.List(fields.String(), required=True)
    resize = fields.Nested(ResizeValidateSchema, many=False)
    architectures = fields.List(
        fields.Nested(ArchitectureValidateSchema), required=True
    )
