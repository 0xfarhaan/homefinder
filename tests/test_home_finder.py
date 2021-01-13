import pytest
from app.home_finder import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get("/")
    assert b"Home Finder" in rv.data
    assert rv.status_code == 200


def test_postcode(client):
    data = {"office_postcode": "W1A1ER", "commute_time": "60"}
    rv = client.post("/postcodes/", data=data)
    assert b"N8" in rv.data
    assert rv.status_code == 200
