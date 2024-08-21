from flask import request, jsonify, Blueprint
from app.services.customer_service import CustomerService

class CustomerController:
    def __init__(self):
        self.customer_service = CustomerService()

    def create_customer(self):
        data = request.json
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password = data.get("password")

        success = self.customer_service.create_customer(
            email, password, first_name, last_name
        )

        if success:
            return jsonify({"message": "Customer created successfully!"}), 201
        else:
            return jsonify({"message": "Failed to create customer"}), 400

    def get_customer_by_id(self, customer_id):
        customer = self.customer_service.get_customer_by_id(customer_id)
        if customer:
            return jsonify(
                {"message": "Customer retrieved successfully", "data": customer}
            )
        return jsonify({"message": "Customer not found"}), 404

    def get_all_customers(self):
        customers = self.customer_service.get_all_customers()
        return jsonify(
            {"message": "Customers retrieved successfully", "data": customers}
        )
        
    def get_customer_by_email_and_password(self):
        data = request.json
        email = data.get("email")
        password = data.get("password")
        customer = self.customer_service.get_customer_by_email(email, password)
        
        if customer is None:
            return jsonify({"message": "Customer not found"}), 404
        elif customer[1] != password:
            return jsonify({"message": "Invalid password"}), 400
        else:
            return jsonify(
                {"message": "Customer retrieved successfully", "data": customer}
            )

# Create an instance of CustomerController
customer_controller = CustomerController()

# Define the blueprint
customer_bp = Blueprint("customer", __name__)

# Define the routes
customer_bp.route("/add", methods=["POST"])(customer_controller.create_customer)
customer_bp.route("/<int:customer_id>", methods=["GET"])(customer_controller.get_customer_by_id)
customer_bp.route("/login", methods=["POST"])(customer_controller.get_customer_by_email_and_password)
customer_bp.route("/getall", methods=["GET"])(customer_controller.get_all_customers)

