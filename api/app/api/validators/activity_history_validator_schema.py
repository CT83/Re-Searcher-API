from marshmallow import Schema, ValidationError, fields, validate, validates
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.activity_history import ActivityHistory
from shared.factories import db


class ActivityHistoryValidatorSchema(Schema):

    """ this schema is for serializing and validating data from post request """

    action_type = fields.String(required=True)
    description = fields.String(required=True)
    arch_id = fields.Int(required=True)
    project_id = fields.Int(required=True)
    user_email = fields.Email(required=True)

    @validates("action_type")
    def validate_action_type(self, action_type):
        action_type_set = {"stop_training", "start_training"}
        if action_type not in action_type_set:
            raise ValidationError("Invalid action type.")

    @validates("arch_id")
    def validate_arch_id(self, arch_id):
        from models.architecture import Architecture

        arch = Architecture.query.filter_by(id=arch_id).first()
        if not arch:
            raise ValidationError("Architecture doesn't exist. ")

    @validates("project_id")
    def validate_project_id(self, project_id):
        from models.project import Project

        project = Project.query.filter_by(id=project_id).first()
        if not project:
            raise ValidationError("Project doesn't exist. ")

