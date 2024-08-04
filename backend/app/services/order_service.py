from app.repositories.order_repository import OrderRepository


class OrderService:
    def __init__(self):
        self.order_repository = OrderRepository()

    def create_order(self, customer_id, seller_id, total_price, products):
        if self.order_repository.create_order(
            customer_id, seller_id, total_price, products
        ):
            return True

    def get_orders_by_customer(self, customer_id):
        return self.order_repository.get_orders_by_customer(customer_id)

    def get_orders_by_seller(self, seller_id):
        return self.order_repository.get_orders_by_seller(seller_id)

    def get_order_details_by_order_id(self, order_id):
        return self.order_repository.get_order_details_by_order_id(order_id)

    def close(self):
        self.order_repository.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
