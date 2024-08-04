from flask import request, jsonify, Blueprint
from app.services.comment_service import CommentService

# Define the blueprint
comment_bp = Blueprint("comment", __name__)

@comment_bp.route("/add", methods=["POST"])
def create_comment():
    data = request.json
    product_id = data.get("product_id")
    customer_id = data.get("customer_id")
    text = data.get("text", None)
    
    with CommentService() as comment_service:
        success = comment_service.create_comment(product_id, customer_id, text)
        if success:
            return jsonify({"message": "Comment created successfully!"}), 201
        else:
            return jsonify({"message": "An error occurred!"}), 500


@comment_bp.route("/<int:comment_id>", methods=["GET"])
def get_comment_by_id(comment_id):
    with CommentService() as comment_service:
        comment = comment_service.get_comment_by_id(comment_id)
        if comment:
            return jsonify({"message": "Comment retrieved successfully", "data": comment})
        return jsonify({"message": "Comment not found"}), 404


@comment_bp.route("/get_by_product/<int:product_id>", methods=["GET"])
def get_comments_by_product(product_id):
    with CommentService() as comment_service:
        comments = comment_service.get_comments_by_product(product_id)
        return jsonify({"message": "Comments retrieved successfully", "data": comments})


@comment_bp.route("/get_by_customer/<int:customer_id>", methods=["GET"])
def get_comments_by_customer(customer_id):
    with CommentService() as comment_service:
        comments = comment_service.get_comments_by_customer(customer_id)
        return jsonify({"message": "Comments retrieved successfully", "data": comments})
