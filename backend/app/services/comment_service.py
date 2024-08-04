from app.repositories.comment_repository import CommentRepository


class CommentService:
    def __init__(self):
        self.comment_repository = CommentRepository()

    def create_comment(self, product_id, customer_id, rate, text=None):
        if self.comment_repository.create_comment(product_id, customer_id, rate, text):
            return True

    def get_comment_by_id(self, comment_id):
        return self.comment_repository.get_comment_by_id(comment_id)

    def get_comments_by_product_id(self, product_id):
        return self.comment_repository.get_comments_by_product_id(product_id)

    def get_comments_by_customer_id(self, customer_id):
        return self.comment_repository.get_comments_by_customer_id(customer_id)

    def close(self):
        self.comment_repository.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
