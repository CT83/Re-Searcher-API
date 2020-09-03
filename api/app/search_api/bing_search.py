import os

import requests


class BingSearch:

    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, search_term):
        """
        Searches Bing API for search_term, pretty simple

        References - https://docs.microsoft.com/en-us/azure/cognitive-services/bing-web-search/quickstarts/python
        :param search_term:
        :return: dict, dict
        """
        search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()

        search_res = search_results.get('webPages').get('value')
        search_res = [{"url": r["url"], "name": r["name"], } for r in search_res]

        if search_results.get('relatedSearches'):
            related_res = search_results.get('relatedSearches').get('value')
            related_res = [{"url": r["webSearchUrl"], "text": r["text"], } for r in related_res]
        else:
            related_res = []

        return search_res, related_res


if __name__ == "__main__":
    bs = BingSearch(api_key=os.environ.get['AZURE_BING_KEY'])
    search_res, related_res = bs.search("Red Mustang")
    print(search_res)
