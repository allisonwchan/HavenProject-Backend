
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = '_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)


# an item
class Product(db.Model):
    name = db.Column(db.String(100), unique = True)
    img = db.Column(db.String(70), unique = True)
    price = db.Column(db.Float)

def __init__(self, name, img, price):
   self.name = name
   self.img = img
   self.price = price

# show what's in the cart
@app.route('/cart')
def show_all():
    return render_template('', items = Product.query.all())


# add an item to cart
@app.route('/add/<product_name>', methods=['POST'])
def add_to_cart(product_name):
    product = Product.query.filter(Product.name==product_name)
    db.session.add(product)
    db.session.commit()
    flash('Item was successfully added to cart')
    return redirect("")
    return render_template('')

# remove item from cart
@app.route('/remove/<product_name>', methods = ['GET', 'POST'])
def delete(product_name):
    product = Product.query.filter(Product.name==product_name)
    if product is None:
        return f'Could not find product in cart'
    db.session.delete(product)
    db.session.commit()
    return redirect("")

# WIP: adding/removing users from db, need to consider user info and the total cost for them...?
@app.route('/newuser', methods = ['GET', 'POST'])
