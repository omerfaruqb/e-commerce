from app.repositories.customer_repository import CustomerRepository


class CustomerService:
    def __init__(self):
        self.customer_repository = CustomerRepository()

    def create_customer(self, email, password, first_name, last_name):
        if self.customer_repository.create_customer(
            email, password, first_name, last_name
        ):
            return True

    def get_customer_by_id(self, id):
        return self.customer_repository.get_customer_by_id(id)

    def get_customer_by_email(self, email):
        return self.customer_repository.get_customer_by_email(email)

    def get_all_customers(self):
        return self.customer_repository.get_all_customers()

    def get_favourite_products(self, customer_id):
        return self.customer_repository.get_favourite_products(customer_id)

    def close(self):
        self.customer_repository.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
