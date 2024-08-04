import psycopg2
from dotenv import load_dotenv, find_dotenv
import os

class CategoriesRepository:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
    
    def create_category(self, category_name):
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO categories (category_name) VALUES (%s);", (category_name,))
            self.conn.commit()
        return True

    def get_category_by_id(self, category_id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM categories WHERE category_id = %s;", (category_id,))
            return cur.fetchone()
        
    def get_all_categories(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM categories;")
            return cur.fetchall()

    def close(self):
        self.conn.close()
