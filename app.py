from flask import Flask, redirect, render_template, request, url_for
from models import db, Product
from api import api

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin@localhost/flask"
app.register_blueprint(api, url_prefix="/api")

@app.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        product = Product(
            request.form["name"], request.form["brand"], request.form["price"]
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html")


@app.route("/delete/<int:id>")
def delete(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):
    product = Product.query.get(id)
    if request.method == "POST":
        product.name = request.form["name"]
        product.brand = request.form["brand"]
        product.price = request.form["price"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", product=product)


if __name__ == "__main__":
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)
