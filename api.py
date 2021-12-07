from flask import Blueprint, Response, request
from models import db, Product
import json

api = Blueprint("api", __name__)

@api.route("/")
def index():
    products = Product.query.all()
    result = [p.to_dict() for p in products]
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@api.route("/add", methods=["POST"])
def add():
    product = Product(request.form["name"], request.form["brand"], request.form["price"])
    db.session.add(product)
    db.session.commit()
    return Response(response=json.dumps({"status": "sucess", "data": product.to_dict()}), status=200, content_type="application/json")

