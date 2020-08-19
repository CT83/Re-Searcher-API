from flask import request
from flask_restful import Resource

from app.api.validators.search_schema import SearchSchema
from app.search_api.factory import create_searcher


class SearchRes(Resource):

    def post(self):
        schema = SearchSchema()
        data = request.json
        errors = schema.validate(data)
        if errors:
            return {"error": True, "errors": errors}, 400

        # Look up in DynamoDB

        # if not search it
        searcher = create_searcher(engine=data["engine"])
        search_res, related_res = searcher.search(data["query"])

        # then save it

        return {"search_res": search_res,
                "related_res": related_res, }

    def get(self):
        return {"msg": {"test"}, }
