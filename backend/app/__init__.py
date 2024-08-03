from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv, find_dotenv
from app.controllers.product_controller import product_bp
from app.controllers.customer_controller import customer_bp

app = Flask(__name__)
load_dotenv(find_dotenv())

app.register_blueprint(product_bp, url_prefix="/products")
app.register_blueprint(customer_bp, url_prefix="/customers")


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello, World!"})

@app.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
