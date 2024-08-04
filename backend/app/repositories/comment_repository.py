import psycopg2
from dotenv import load_dotenv, find_dotenv
import os


class CommentRepository:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )

    def create_comment(self, product_id, customer_id, rate, text=None):
        if text:
            with self.conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO comments (product_id, customer_id, rate, text) VALUES (%s, %s, %s, %s);",
                    (product_id, customer_id, rate, text),
                )
                self.conn.commit()
        else:
            with self.conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO comments (product_id, customer_id, rate) VALUES (%s, %s, %s);",
                    (product_id, customer_id, rate),
                )
                self.conn.commit()
        return True

    def get_comment_by_id(self, comment_id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM comments WHERE comment_id = %s;", (comment_id,))
            return cur.fetchone()

    def get_comments_by_product_id(self, product_id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM comments WHERE product_id = %s;", (product_id,))
            return cur.fetchall()

    def get_comments_by_customer_id(self, customer_id):
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM comments WHERE customer_id = %s;", (customer_id,)
            )
            return cur.fetchall()

    def close(self):
        self.conn.close()
