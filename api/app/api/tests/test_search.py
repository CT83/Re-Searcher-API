import json


def test_mock_search(app):
    client = app.test_client()

    res = client.post(
        "/search",
        json=dict(
            engine="mock",
            query="This is sample text",
        ))
    assert res.status_code == 200
    data = json.loads(res.get_data(as_text=True))
    # project_id = data["id"]
    # assert type(data["results"]) == type
    assert isinstance(data["search_res"], list)

    for res in data["search_res"]:
        assert res["url"]
        assert res["name"]
