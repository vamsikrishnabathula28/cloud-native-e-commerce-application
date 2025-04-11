# Cloud Native E-commerce Application

A modern e-commerce application built with Flask, featuring real-time order monitoring and a responsive dashboard.

## Features

- Product catalog with images
- Shopping cart functionality
- Order placement system
- Real-time order monitoring dashboard
- Sales metrics and analytics
- Responsive design

## Technologies Used

- Python
- Flask
- SQLite
- HTML/CSS/JavaScript
- Chart.js

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cloud-native-ecommerce.git
cd cloud-native-ecommerce
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python server.py
```

4. Open your browser and navigate to:
```
http://127.0.0.1:8000
```

## Project Structure

- `server.py` - Main Flask application
- `database.py` - Database operations
- `index.html` - Homepage with product catalog
- `cart.html` - Shopping cart page
- `dashboard.html` - Real-time order monitoring dashboard
- `styles.css` - Global styles

## API Endpoints

- `GET /api/products` - Get all products
- `POST /api/order` - Place a new order
- `GET /api/order-history` - Get order history
- `GET /api/metrics` - Get sales metrics

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License. 