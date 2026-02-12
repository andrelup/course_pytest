

def test_healthcheck(client):
    response = client.get("/commons/healthcheck")
    assert response.status_code == 200 and response.json() == {"status": "on"}