from marshmallow import Schema, fields


class SearchSchema(Schema):
    engine = fields.Str(required=True)
    query = fields.Str(required=True)
