from fastapi.testclient import TestClient

from auth import API_KEY
from main import app

client = TestClient(app)


def test_create_extraction():
    with open("test.pdf", "rb") as f:
        response = client.post(
            "/extractions",
            headers={"x-api-key": API_KEY},
            files={"file": ("test.pdf", f, "application/pdf")},
        )

    assert response.status_code == 201
    data = response.json()
    assert data["filename"] == "test.pdf"
    assert data["status"] in ["completed", "failed"]

def test_create_extraction_sans_cle_api():
    with open("test.pdf", "rb") as f:
        response = client.post(
            "/extractions",
            files={"file": ("test.pdf", f, "application/pdf")},
        )

    assert response.status_code == 422


def test_create_extraction_mauvaise_cle_api():
    with open("test.pdf", "rb") as f:
        response = client.post(
            "/extractions",
            headers={"x-api-key": "fausse-cle"},
            files={"file": ("test.pdf", f, "application/pdf")},
        )

    assert response.status_code == 401