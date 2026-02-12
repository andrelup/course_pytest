from src.settings.environment import EnvironmentSettings

def test_healthcheck(client):
    response = client.get("/commons/healthcheck")
    assert response.status_code == 200 and response.json() == {"status": "on"}

def test_environment(client):
    response = client.get("/commons/environment")
    assert response.status_code == 200 and response.json() == {"environment": EnvironmentSettings.ENVIRONMENT}