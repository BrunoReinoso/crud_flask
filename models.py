from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True, unique=True)
    name = db.Column(db.String(20), unique=True)
    brand = db.Column(db.String(20))
    price = db.Column(db.Float)

    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price
    
    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "name": self.name, "brand": self.brand, "price": self.price}
        else:
            return {col: getattr(self,col) for col in columns}