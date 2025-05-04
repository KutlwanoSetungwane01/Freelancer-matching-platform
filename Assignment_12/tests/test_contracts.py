from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_contract():
    response = client.post("/contracts/", json={
        "id": 1,
        "job_post_id": 1,
        "freelancer_id": 100,
        "employer_id": 200,
        "terms": "Project to be completed in 2 weeks.",
        "status": "active"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "active"

def test_get_all_contracts():
    response = client.get("/contracts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_contract_by_id():
    response = client.get("/contracts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
