import pytest
from starlette.testclient import TestClient
from main import app
from pytest import fixture


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  


