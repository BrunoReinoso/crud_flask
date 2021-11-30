from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/flask'

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True, unique=True)
    name = db.Column(db.String(20), unique=True)
    price = db.Column(db.Float) 
    
    def __init__ (self, name, price):
        self.name = name
        self.price = price

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)