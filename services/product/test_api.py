import requests
import json

# Base URL for the product service
BASE_URL = "http://localhost:8000"

def print_response(response):
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(json.dumps(response.json(), indent=2))
    print("-" * 50)

def test_product_api():
    # Create a new product
    print("1. Creating a new product:")
    product_data = {
        "name": "Smartphone X",
        "description": "Latest smartphone with advanced features",
        "price": 999.99,
        "stock": 100,
        "category": "Electronics",
        "image_url": "https://example.com/smartphone-x.jpg"
    }
    response = requests.post(f"{BASE_URL}/products/", json=product_data)
    print_response(response)
    product_id = response.json()["id"]

    # Get all products
    print("\n2. Getting all products:")
    response = requests.get(f"{BASE_URL}/products/")
    print_response(response)

    # Get a specific product
    print(f"\n3. Getting product with ID {product_id}:")
    response = requests.get(f"{BASE_URL}/products/{product_id}")
    print_response(response)

    # Update a product
    print(f"\n4. Updating product with ID {product_id}:")
    update_data = {
        "name": "Smartphone X Pro",
        "price": 1099.99,
        "stock": 50
    }
    response = requests.put(f"{BASE_URL}/products/{product_id}", json=update_data)
    print_response(response)

    # Health check
    print("\n5. Health check:")
    response = requests.get(f"{BASE_URL}/health")
    print_response(response)

if __name__ == "__main__":
    test_product_api() 