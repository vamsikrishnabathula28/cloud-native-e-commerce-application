from flask import Flask, jsonify, request, send_from_directory
import os
import webbrowser
from threading import Timer
from database import save_order, get_order_history, get_sales_metrics, init_db

app = Flask(__name__, static_folder='.')

# Sample product data with image URLs
products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"},
    {"id": 2, "name": "Smartphone", "price": 699.99, "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"},
    {"id": 3, "name": "Headphones", "price": 199.99, "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"},
    {"id": 4, "name": "Tablet", "price": 499.99, "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"},
    {"id": 5, "name": "Smartwatch", "price": 299.99, "image": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"}
]

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/cart.html')
def cart():
    return send_from_directory('.', 'cart.html')

@app.route('/dashboard.html')
def dashboard():
    return send_from_directory('.', 'dashboard.html')

@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css')

@app.route('/api/products')
def get_products():
    return jsonify(products)

@app.route('/api/order', methods=['POST'])
def create_order():
    data = request.json
    for item in data['items']:
        product = next(p for p in products if p['id'] == item['id'])
        save_order(product['id'], product['name'], item['quantity'], product['price'])
    return jsonify({"message": "Order placed successfully"})

@app.route('/api/order-history')
def order_history():
    orders = get_order_history()
    return jsonify(orders)

@app.route('/api/metrics')
def sales_metrics():
    metrics = get_sales_metrics()
    return jsonify(metrics)

def open_browser():
    webbrowser.open('http://127.0.0.1:8000')

if __name__ == '__main__':
    # Initialize database
    init_db()
    # Open browser after a short delay
    Timer(1.5, open_browser).start()
    # Start the server
    app.run(port=8000) 