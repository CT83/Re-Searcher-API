from flask_restful import Resource


class SearchRes(Resource):

    def post(self):

        # Look up in DynamoDB

        # if not search it

        # then save it

        return {"message": "Job added to queue",
                "job_id": 0, }

    def get(self):
        return {"msg": {"test"}, }
