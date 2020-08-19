from marshmallow import Schema, fields
from app.api.validators.resize_validate_schema import ResizeValidateSchema


class ArchitectureValidateSchema(Schema):

    """ this schema is for validating data from post request """

    name = fields.String(required=True)
    backbone = fields.String(required=True)
    batch_size = fields.Int(required=True)
    epochs = fields.Int(required=True)
    num_gpus = fields.Int(required=True)
    worker_ids = fields.List(fields.Int(), required=True)

    pretrained_model = fields.String(required=False)
    epochs_limit = fields.Int(required=False)
    readable_name = fields.String(required=False)

    title = fields.String(required=True, default="")
    description = fields.String(required=True, default="")

    api_key = fields.String(required=False)
    tags = fields.List(fields.String(), required=False)
    classes = fields.List(fields.String(), required=False)
    resize = fields.Nested(ResizeValidateSchema, many=False)
    dataset = fields.String(required=False)
