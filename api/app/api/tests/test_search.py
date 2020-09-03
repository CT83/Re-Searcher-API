import json


def test_mock_search_get(app):
    client = app.test_client()

    res = client.get("/search?query=Cars", )
    assert res.status_code == 200
    data = json.loads(res.get_data(as_text=True))
    assert isinstance(data["search_res"], list)

    for res in data["search_res"]:
        assert res["url"]
        assert res["name"]
