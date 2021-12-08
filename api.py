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
    return Response(response=json.dumps({"status": "sucess", "data": product.to_dict()}), status=201, content_type="application/json")

@api.route("/delete/<int:id>")
def delete(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return Response(response=json.dumps({"status": "deleted"}), status=200, content_type="application/json")

@api.route("/edit/<int:id>", methods=["POST"])
def edit(id):
    product = Product.query.get(id)
    product.name = request.form["name"]
    product.brand = request.form["brand"]
    product.price = request.form["price"]
    db.session.commit()
    return Response(response=json.dumps({"status": "modified", "data": product.to_dict()}), status=200, content_type="application/json")
    