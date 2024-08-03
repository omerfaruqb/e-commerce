import psycopg2
import os


class ProductRepository:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
        )

    def create_product(self, name, description, unit_price, category_id, seller_id):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO products (name, description, unit_price, category_id, seller_id) VALUES (%s, %s, %s, %s, %s);",
                (name, description, unit_price, category_id, seller_id),
            )
            self.conn.commit()

    def get_product_by_id(self, product_id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM products WHERE product_id = %s;", (product_id,))
            data = cur.fetchone()

        return data

    def get_products_by_category(self, category_id):
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM products WHERE category_id = %s;", (category_id,)
            )
            data = cur.fetchall()

        return data

    def get_products_by_seller(self, seller_id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM products WHERE seller_id = %s;", (seller_id,))
            data = cur.fetchall()

        return data

    def get_all_products(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM products;")
            data = cur.fetchall()

        return data

    def __delete__(self):
        self.conn.close()
