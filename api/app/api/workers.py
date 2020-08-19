from flask import request
from flask_restful import Resource

# from app.api.serializers.worker_schema import WorkerSchema
# from models import Worker
from shared.factories import db


class Workers(Resource):

    def post(self):
        # schema = WorkerSchema()
        # data = request.json
        # errors = schema.validate(data, session=db.session)
        # if errors:
        #     return {"error": True, "errors": errors}, 400
        # work = Worker(**data)
        # db.session.add(work)
        # db.session.commit()
        # res = work.as_dict()
        # print(work)
        # res["message"] = "New Worker Created Successfully!"
        return res

    def put(self, index):
        action = request.get_json()['action']
        if action:
            raise NotImplementedError("This is yet to be implemented.")

    def delete(self, index):
        Worker.query.filter_by(id=index).delete()
        db.session.commit()
        res = {"message": "Deleted Worker Successfully!"}
        return res

    def get(self, index=None):
        if index:
            worker = Worker.query.filter_by(id=index).first()
            return worker.as_dict()
        else:
            archis = [b.as_dict() for b in Worker.query.all()]
            return {"workers": archis}
