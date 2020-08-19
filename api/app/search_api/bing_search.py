import requests


class BingSearch:

    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, search_term):
        search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()

        search_res = search_results.get('webPages').get('value')
        related_res = search_results.get('relatedSearches').get('value')

        search_res = [{"url": r["url"], "name": r["name"], } for r in search_res]
        related_res = [{"url": r["webSearchUrl"], "text": r["text"], } for r in related_res]
        return search_res, related_res


if __name__ == "__main__":
    bs = BingSearch(api_key="d228414bc5714963a7d032af6e7c88e3")
    search_res, related_res = bs.search("Red Mustang")
    print(search_res)
