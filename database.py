import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    
    # Create orders table
    c.execute('''CREATE TABLE IF NOT EXISTS orders
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  product_id INTEGER,
                  product_name TEXT,
                  quantity INTEGER,
                  price REAL,
                  timestamp DATETIME)''')
    
    conn.commit()
    conn.close()

def save_order(product_id, product_name, quantity, price):
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    
    c.execute('''INSERT INTO orders (product_id, product_name, quantity, price, timestamp)
                 VALUES (?, ?, ?, ?, ?)''',
              (product_id, product_name, quantity, price, datetime.now()))
    
    conn.commit()
    conn.close()

def get_order_history():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    
    c.execute('''SELECT * FROM orders ORDER BY timestamp DESC''')
    orders = c.fetchall()
    
    conn.close()
    return orders

def get_sales_metrics():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    
    # Get total sales
    c.execute('''SELECT SUM(price * quantity) FROM orders''')
    total_sales = c.fetchone()[0] or 0
    
    # Get total orders
    c.execute('''SELECT COUNT(*) FROM orders''')
    total_orders = c.fetchone()[0] or 0
    
    # Get average order value
    c.execute('''SELECT AVG(price * quantity) FROM orders''')
    avg_order_value = c.fetchone()[0] or 0
    
    # Get top selling products
    c.execute('''SELECT product_name, SUM(quantity) as total_quantity
                 FROM orders
                 GROUP BY product_name
                 ORDER BY total_quantity DESC
                 LIMIT 5''')
    top_products = c.fetchall()
    
    conn.close()
    return {
        'total_sales': total_sales,
        'total_orders': total_orders,
        'avg_order_value': avg_order_value,
        'top_products': top_products
    }

# Initialize database when module is imported
init_db() 