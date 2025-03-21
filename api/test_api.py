import time
import requests

BASE_URL = "http://127.0.0.1:8000"

# Optimized Polling
MAX_ATTEMPTS = 10  # Reduce total attempts
WAIT_TIME = 2  # Lower wait time (total 10 * 2 = 20 sec max wait)


def create_model():
    """Helper function to create a new model."""
    response = requests.post(f"{BASE_URL}/models/", json={"name": "TestModel"})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()
    assert "id" in data, "Response must contain 'id'"
    assert data["status"] == "PROCESSING", "Model should start in 'PROCESSING' state"
    
    return data["id"]


def test_create_model():
    """Test creating a new model"""
    model_id = create_model()
    assert isinstance(model_id, str), "Model ID should be a string"

def test_list_models():
    """Test retrieving the list of models"""
    response = requests.get(f"{BASE_URL}/models/")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()
    assert isinstance(data, list), "Response should be a list of models"
    if data:
        assert "id" in data[0], "Model objects should have 'id'"
        assert "status" in data[0], "Model objects should have 'status'"

def test_get_model():
    """Test retrieving a model by ID"""
    model_id = create_model()
    response = requests.get(f"{BASE_URL}/models/{model_id}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()
    assert data["id"] == model_id, "Returned model ID should match the requested ID"
    assert data["name"] == "TestModel", "Returned model name should be correct"

def test_get_nonexistent_model():
    """Test retrieving a model that does not exist"""
    response = requests.get(f"{BASE_URL}/models/invalid-id")
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"

def test_get_nonexistent_model_results():
    """Test retrieving results of a non-existent model"""
    response = requests.get(f"{BASE_URL}/models/invalid-id/data")
    assert response.status_code == 500, f"Expected 500, got {response.status_code}"
