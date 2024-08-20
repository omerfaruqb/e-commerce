from flask import request, jsonify, Blueprint
from app.services.product_service import ProductService

# Define the blueprint
product_bp = Blueprint("product", __name__)

class ProductController:
    def __init__(self):
        self.product_service = ProductService()

    def create_product(self):
        data = request.json
        name = data.get("name")
        description = data.get("description", "")
        unit_price = data.get("unit_price")
        category_id = data.get("category_id")
        seller_id = data.get("seller_id")

        success = self.product_service.create_product(
            name, description, unit_price, category_id, seller_id
        )
        if success:
            return jsonify({"message": "Product created successfully!"}), 201
        else:
            return jsonify({"message": "An error occurred!"}), 500

    def get_product_by_id(self, product_id):
        product = self.product_service.get_product_by_id(product_id)
        if product:
            return jsonify(
                {"message": "Product retrieved successfully", "data": product}
            )
        return jsonify({"message": "Product not found"}), 404

    def get_all_products(self):
        products = self.product_service.get_all_products()
        return jsonify({"message": "Products retrieved successfully", "data": products})

    def get_products_by_category(self, category_id):
        products = self.product_service.get_products_by_category(category_id)
        return jsonify({"message": "Products retrieved successfully", "data": products})

# Create an instance of the ProductController
product_controller = ProductController()

# Define the routes
product_bp.route("/add", methods=["POST"])(product_controller.create_product)
product_bp.route("/<int:product_id>", methods=["GET"])(product_controller.get_product_by_id)
product_bp.route("/getall", methods=["GET"])(product_controller.get_all_products)
product_bp.route("get_by_category/<int:category_id>", methods=["GET"])(product_controller.get_products_by_category)
