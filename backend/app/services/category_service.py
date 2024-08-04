from app.repositories.category_repository import CategoryRepository


class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def create_category(self, category_name):
        if self.category_repository.create_category(category_name):
            return True

    def get_category_by_id(self, category_id):
        return self.category_repository.get_category_by_id(category_id)

    def get_all_categories(self):
        return self.category_repository.get_all_categories()

    def close(self):
        self.category_repository.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
