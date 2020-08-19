from flask import current_app

from app.search_api.mock_search import MockSearch


def create_searcher(engine):
    """Creates a searcher of the requested type"""
    if engine == "bing":
        from app.search_api.bing_search import BingSearch
        return BingSearch(api_key=current_app.config['AZURE_BING_KEY'])
    elif engine == "mock":
        return MockSearch() # more searchers can be easily added here
    else:
        raise NotImplementedError("{} is not implemented!".format(engine))
