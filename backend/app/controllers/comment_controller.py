from flask import request, jsonify, Blueprint
from app.services.comment_service import CommentService

# Define the blueprint
comment_bp = Blueprint("comment", __name__)

class CommentController:
    def __init__(self):
        self.comment_service = CommentService()

    def create_comment(self):
        data = request.json
        product_id = data.get("product_id")
        customer_id = data.get("customer_id")
        text = data.get("text", None)

        success = self.comment_service.create_comment(product_id, customer_id, text)
        if success:
            return jsonify({"message": "Comment created successfully!"}), 201
        else:
            return jsonify({"message": "An error occurred!"}), 500

    def get_comment_by_id(self, comment_id):
        comment = self.comment_service.get_comment_by_id(comment_id)
        if comment:
            return jsonify({"message": "Comment retrieved successfully", "data": comment})
        return jsonify({"message": "Comment not found"}), 404

    def get_comments_by_product(self, product_id):
        comments = self.comment_service.get_comments_by_product(product_id)
        return jsonify({"message": "Comments retrieved successfully", "data": comments})

    def get_comments_by_customer(self, customer_id):
        comments = self.comment_service.get_comments_by_customer(customer_id)
        return jsonify({"message": "Comments retrieved successfully", "data": comments})

# Create an instance of the CommentController
comment_controller = CommentController()

# Define the routes
comment_bp.route("/add", methods=["POST"])(comment_controller.create_comment)
comment_bp.route("/<int:comment_id>", methods=["GET"])(comment_controller.get_comment_by_id)
comment_bp.route("/get_by_product/<int:product_id>", methods=["GET"])(comment_controller.get_comments_by_product)
comment_bp.route("/get_by_customer/<int:customer_id>", methods=["GET"])(comment_controller.get_comments_by_customer)
