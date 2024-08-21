from flask import request, jsonify, Blueprint
from app.services.seller_service import SellerService

# Define the blueprint
seller_bp = Blueprint("seller", __name__)

class SellerController:
    def __init__(self):
        self.seller_service = SellerService()

    def create_seller(self):
        data = request.json
        email = data.get("email")
        password = data.get("password")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        company_name = data.get("company_name")

        success = self.seller_service.create_seller(
            email, password, first_name, last_name, company_name
        )
        if success:
            return jsonify({"message": "Seller created successfully!"}), 201
        else:
            return jsonify({"message": "An error occurred!"}), 500

    def get_seller_by_id(self, seller_id):
        seller = self.seller_service.get_seller_by_id(seller_id)
        if seller:
            return jsonify({"message": "Seller retrieved successfully", "data": seller})
        return jsonify({"message": "Seller not found"}), 404

    def get_seller_by_email(self, email):
        seller = self.seller_service.get_seller_by_email(email)
        if seller:
            return jsonify({"message": "Seller retrieved successfully", "data": seller})
        return jsonify({"message": "Seller not found"}), 404

# Create an instance of the SellerController
seller_controller = SellerController()

# Define the routes
seller_bp.route("/add", methods=["POST"])(seller_controller.create_seller)
seller_bp.route("/<int:seller_id>", methods=["GET"])(seller_controller.get_seller_by_id)
seller_bp.route("/get_seller_by_email/<string:email>", methods=["GET"])(seller_controller.get_seller_by_email)
