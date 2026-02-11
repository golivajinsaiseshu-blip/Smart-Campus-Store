from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    min_stock_level = db.Column(db.Integer, default=5)
    batches = db.relationship('Batch', backref='product_info', lazy=True)
    sales = db.relationship('Sale', backref='product_sold', lazy=True) # New Relationship

class Batch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)

# --- ADD THIS TABLE NOW ---
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity_sold = db.Column(db.Integer, default=1)
    sale_date = db.Column(db.DateTime, default=datetime.utcnow)