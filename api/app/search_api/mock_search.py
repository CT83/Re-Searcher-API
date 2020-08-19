import random

from shared.utils import generate_random_string


class MockSearch:

    """
    This is a mock Searcher, which can be used for testing
    """

    def search(self, search_term):
        search_res = [{"url": "http://{}".format(generate_random_string()),
                       "name": generate_random_string(), } for _ in range(random.randint(1, 10))]
        related_res = [{"url": "http://{}".format(generate_random_string()),
                        "text": generate_random_string(), } for _ in range(random.randint(1, 10))]
        return search_res, related_res


if __name__ == "__main__":
    ms = MockSearch()
    search_res, related_res = ms.search("Red Mustang")
    print(search_res)
