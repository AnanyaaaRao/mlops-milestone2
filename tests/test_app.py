from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home_endpoint():
    """
    Basic health check:
    Ensures the API is running and returns expected metadata.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"
    assert response.json()["message"] == "Iris Prediction API"


def test_predict_endpoint_valid_input():
    """
    Core functionality test:
    Ensures the /predict endpoint returns a valid prediction
    for correct input shape.
    """
    payload = {
        "features": [5.1, 3.5, 1.4, 0.2]
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "prediction" in data
    assert "model_version" in data

    # Iris dataset has 3 classes: 0, 1, 2
    assert data["prediction"] in [0, 1, 2]
    assert data["model_version"] == "v1.0.0"