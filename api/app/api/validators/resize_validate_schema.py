from marshmallow import Schema, fields


class ResizeValidateSchema(Schema):
    width = fields.Int(required=True)
    height = fields.Int(required=True)
    padding = fields.Bool(required=True, default=True)
