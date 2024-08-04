from app.repositories.seller_repository import SellerRepository


class SellerService:
    def __init__(self):
        self.seller_repository = SellerRepository()

    def create_seller(self, email, password, first_name, last_name, company_name):
        if self.seller_repository.create_seller(
            email, password, first_name, last_name, company_name
        ):
            return True

    def get_seller_by_email(self, email):
        return self.seller_repository.get_seller_by_email(email)

    def get_seller_by_id(self, seller_id):
        return self.seller_repository.get_seller_by_id(seller_id)

    def close(self):
        self.seller_repository.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
