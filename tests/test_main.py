from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "API en ligne"}


def test_my_cicd():
    response = client.get("/mycicd")

    assert response.status_code == 200
    assert response.json() == {"message": "ci et cd sont prets a 100 %"}

def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}