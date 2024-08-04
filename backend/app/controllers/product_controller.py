from flask import request, jsonify, Blueprint
from app.services.product_service import ProductService

# Define the blueprint
product_bp = Blueprint("product", __name__)


# Define the routes
@product_bp.route("/add", methods=["POST"])
def create_product():
    data = request.json
    name = data.get("name")
    description = data.get("description", "")
    unit_price = data.get("unit_price")
    category_id = data.get("category_id")
    seller_id = data.get("seller_id")

    with ProductService() as product_service:
        success = product_service.create_product(
            name, description, unit_price, category_id, seller_id
        )
        if success:
            return jsonify({"message": "Product created successfully!"}), 201
        else:
            return jsonify({"message": "An error occurred!"}), 500


@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    with ProductService() as product_service:
        product = product_service.get_product_by_id(product_id)
        if product:
            return jsonify(
                {"message": "Product retrieved succesfully", "data": product}
            )
        return jsonify({"message": "Product not found"}), 404


@product_bp.route("/getall", methods=["GET"])
def get_all_products():
    with ProductService() as product_service:
        products = product_service.get_all_products()
        return jsonify({"message": "Products retrieved succesfully", "data": products})


@product_bp.route("get_by_category/<int:category_id>", methods=["GET"])
def get_products_by_category(category_id):
    with ProductService() as product_service:
        products = product_service.get_products_by_category(category_id)
        return jsonify({"message": "Products retrieved successfully", "data": products})
