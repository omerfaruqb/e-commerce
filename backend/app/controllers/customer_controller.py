from flask import request, jsonify, Blueprint
from app.services.customer_service import CustomerService

# Define the blueprint
customer_bp = Blueprint("customer", __name__)


# Define the routes
@customer_bp.route("/add", methods=["POST"])
def create_customer():
    data = request.form
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    password = data.get("password")

    with CustomerService() as customer_service:
        success = customer_service.create_customer(
            first_name, last_name, email, password
        )
        if success:
            return jsonify({"message": "Customer created successfully!"}), 201
        else:
            return jsonify({"message": "An error occurred!"}), 500


@customer_bp.route("/<int:customer_id>", methods=["GET"])
def get_customer_by_id(customer_id):
    with CustomerService() as customer_service:
        customer = customer_service.get_customer_by_id(customer_id)
        if customer:
            return jsonify(
                {"message": "Customer retrieved succesfully", "data": customer}
            )
        return jsonify({"message": "Customer not found"}), 404


@customer_bp.route("/getall", methods=["GET"])
def get_all_customers():
    with CustomerService() as customer_service:
        customers = customer_service.get_all_customers()
        return jsonify(
            {"message": "Customers retrieved succesfully", "data": customers}
        )
