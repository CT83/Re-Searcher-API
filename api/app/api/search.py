from flask import request
from flask_restful import Resource

from app.api.validators.search_schema import SearchSchema
from app.search_api.factory import create_searcher
from models.search_results import Results, SearchRequests


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
        results = [Results(name=res["name"], url=res["url"]) for res in search_res]
        s = SearchRequests(query=data["query"], results=results)
        s.save()

        return {"search_res": search_res,
                "related_res": related_res, }

    def get(self):
        no_searches = SearchRequests.count()

        return {"count": no_searches, }
