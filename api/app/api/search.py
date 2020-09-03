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

    def get(self):
        args = request.args
        query = str(args['query'])
        engine = 'bing'

        # Look up in DynamoDB
        stored_res = SearchRequests.query(query, SearchRequests.engine_text == engine)
        stored_res = list(stored_res)
        if stored_res:  # if found return that
            stored_res = stored_res[0]
            search_res = [{"url": res.url, "name": res.name}
                          for res in stored_res.results]
        else:  # else perform a search
            searcher = create_searcher(engine=engine)
            search_res, related_res = searcher.search(query)

            # then save it
            results = [Results(name=res["name"], url=res["url"]) for res in search_res]
            s = SearchRequests(query_text=query, engine_text=engine, results=results)
            s.save()

        return {"search_res": search_res}


class SupportedEnginesRes(Resource):

    def get(self):
        return {"supported_engines": ["bing", "mock"]}
