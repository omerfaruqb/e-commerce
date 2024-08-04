from flask import request, jsonify, Blueprint
from app.services.seller_service import SellerService

# Define the blueprint
seller_bp = Blueprint("seller", __name__)


@seller_bp.route("/add", methods=["POST"])
def create_seller():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    company_name = data.get("company_name")

    with SellerService() as seller_service:
        success = seller_service.create_seller(
            first_name, last_name, email, password, company_name
        )
        if success:
            return jsonify({"message": "Seller created successfully!"}), 201
        else:
            return jsonify({"message": "An error occurred!"}), 500


@seller_bp.route("/<int:seller_id>", methods=["GET"])
def get_seller_by_id(seller_id):
    with SellerService() as seller_service:
        seller = seller_service.get_seller_by_id(seller_id)
        if seller:
            return jsonify({"message": "Seller retrieved successfully", "data": seller})
        return jsonify({"message": "Seller not found"}), 404


@seller_bp.route("/get_seller_by_email/<string:email>", methods=["GET"])
def get_seller_by_email(email):
    with SellerService() as seller_service:
        seller = seller_service.get_seller_by_email(email)
        if seller:
            return jsonify({"message": "Seller retrieved successfully", "data": seller})
        return jsonify({"message": "Seller not found"}), 404
