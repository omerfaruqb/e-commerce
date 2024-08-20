from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
from app.controllers.product_controller import product_bp
from app.controllers.customer_controller import customer_bp
from app.controllers.comment_controller import comment_bp
from app.controllers.seller_controller import seller_bp

app = Flask(__name__)
CORS(app)
load_dotenv(find_dotenv())

app.register_blueprint(product_bp, url_prefix="/products")
app.register_blueprint(customer_bp, url_prefix="/customers")
app.register_blueprint(comment_bp, url_prefix="/comments")
app.register_blueprint(seller_bp, url_prefix="/sellers")

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello, World!"})

@app.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
