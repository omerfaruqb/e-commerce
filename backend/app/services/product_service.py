from app.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def create_product(self, name, description, unit_price, category_id, seller_id):
        if self.product_repository.create_product(
            name, description, unit_price, category_id, seller_id
        ):
            return True

    def get_product_by_id(self, product_id):
        return self.product_repository.get_product_by_id(product_id)

    def get_products_by_category(self, category_id):
        return self.product_repository.get_products_by_category(category_id)

    def get_products_by_seller(self, seller_id):
        return self.get_products_by_seller(seller_id)

    def get_all_products(self):
        return self.product_repository.get_all_products()

    def close(self):
        self.product_repository.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
