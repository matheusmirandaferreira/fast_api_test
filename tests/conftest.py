import pytest
from fastapi.testclient import TestClient
from fast_api_test.app import app


@pytest.fixture()
def client():
  return TestClient(app)