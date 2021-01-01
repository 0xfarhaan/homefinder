import pytest
from app.home_finder import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    print(rv.data)
    assert b"Home Finder" in rv.data

