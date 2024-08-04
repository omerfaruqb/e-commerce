import psycopg2
from dotenv import load_dotenv, find_dotenv
import os

class OrderRepository:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
    
    def create_order(self, customer_id, seller_id, total_price, products):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO orders (customer_id, seller_id, total_price, order_date) VALUES (%s, %s, NOW()) RETURNING customer_id;",
                (customer_id, seller_id, total_price)
            )
            order_id = cur.fetchone()[0]
            cur.execute(
                "INSERT INTO order_details (product_id, order_id, unit_price, quantity, cargo_state) VALUES %s;",
                [(product['product_id'], order_id, product['unit_price'], product['quantity'], 'Preparing...') for product in products]
            )
            self.conn.commit()
        return True

    def get_orders_by_customer(self, customer_id):
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM orders WHERE customer_id = %s;",
                (customer_id,)
            )

    def get_orders_by_seller(self, seller_id):
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM orders WHERE seller_id = %s;",
                (seller_id,)
            )

    def get_order_details_by_order_id(self, order_id):
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM order_details WHERE order_id = %s;",
                (order_id,)
            )
            return cur.fetchall()
            

    def close(self):
        self.conn.close()