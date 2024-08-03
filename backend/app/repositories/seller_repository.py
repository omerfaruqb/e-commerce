import os
import psycopg2


class SellerRepository:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
        )

    def create_seller(self, email, password, first_name, last_name, company_name):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO sellers (email, password, first_name, last_name, company_name, date_joined) VALUES (%s, %s, %s, %s, %s, NOW());",
                (email, password, first_name, last_name, company_name),
            )
            self.conn.commit()

    def get_seller_by_email(self, email):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM sellers WHERE email = %s;", (email,))
            data = cur.fetchone()

        return data

    def get_seller_by_id(self, seller_id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM sellers WHERE seller_id = %s;", (seller_id,))
            data = cur.fetchone()

        return data
    
    def __del__(self):
        self.conn.close()


