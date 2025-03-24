import pytest
import json
from app import app

def test_main():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, Welcome to Receipt Processor Challenge!" in response.data


def test_process_receipts_valid():
    client = app.test_client()
    valid_receipt = {
        "retailer": "Best Buy",
        "purchaseDate": "2023-03-22",
        "purchaseTime": "14:33",
        "items": [{"shortDescription": "Laptop", "price": "999.99"}],
        "total": "999.99"
    }
    response = client.post('/receipts/process', data=json.dumps(valid_receipt), content_type='application/json')
    
    assert response.status_code == 200
    data = response.get_json()
    assert "id" in data

def test_process_receipts_invalid():
    client = app.test_client()
    invalid_receipt = {"invalid": "data"}
    response = client.post('/receipts/process', data=json.dumps(invalid_receipt), content_type='application/json')
    
    assert response.status_code == 400
    data = response.get_json()
    assert data["message"] == "The receipt is invalid."


def test_get_points_valid():
    client = app.test_client()
    valid_receipt = {
        "retailer": "Best Buy",
        "purchaseDate": "2023-03-22",
        "purchaseTime": "14:33",
        "items": [{"shortDescription": "Laptop", "price": "999.99"}],
        "total": "999.99"
    }
    process_response = client.post('/receipts/process', data=json.dumps(valid_receipt), content_type='application/json')
    receipt_id = process_response.get_json()["id"]
    
    response = client.get(f'/receipts/{receipt_id}/points')
    assert response.status_code == 200
    data = response.get_json()
    assert "points" in data

def test_get_points_invalid():
    client = app.test_client()
    response = client.get('/receipts/invalid-id/points')
    
    assert response.status_code == 400
    data = response.get_json()
    assert data["message"] == "No receipt found for that ID."
