import psycopg2
from dotenv import load_dotenv, find_dotenv
import os


class CustomerRepository:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
        )

    def create_customer(self, email, password, first_name, last_name):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO customers (email, password, first_name, last_name) VALUES (%s, %s, %s, %s);",
                (email, password, first_name, last_name),
            )
            self.conn.commit()
        return True

    def get_customer_by_id(self, customer_id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM customers WHERE customer_id = %s;", (customer_id,))
            data = cur.fetchone()

        return data

    def get_customer_by_email(self, email):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM customers WHERE email = %s;", (email,))
            data = cur.fetchone()

        return data

    def get_all_customers(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM customers;")
            data = cur.fetchall()

        return data

    def __del__(self):
        self.conn.close()
