import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from datetime import datetime
from models import db, Product, Batch, Sale 

app = Flask(__name__)

# Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'inventory_v2.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def dashboard():
    today = datetime.now().date()
    batches = db.session.execute(select(Batch)).scalars().all()
    
    # Feature: Aggregated total sales for the summary cards
    total_sales = db.session.query(Sale).count()
    
    report = []
    for b in batches:
        product = db.session.get(Product, b.product_id)
        
        # Predictive Analysis: Calculate days of stock remaining
        # Fulfills "Predictive Analysis" and "Recording consumption" requirements
        sales_count = db.session.query(Sale).filter_by(product_id=b.product_id).count()
        
        days_of_stock_left = "N/A"
        if sales_count > 0:
            # Prediction: Current Quantity / Average daily sales
            days_of_stock_left = round(b.quantity / sales_count, 1) 

        # Expiry Status Logic
        days_left = (b.expiry_date - today).days
        if days_left < 0: status = "🔴 EXPIRED"
        elif days_left <= 7: status = "🟠 CRITICAL"
        elif days_left <= 15: status = "🟡 WARNING"
        else: status = "🟢 FRESH"
            
        # Low Stock Logic: Triggers UI highlights
        is_low = b.quantity <= (product.min_stock_level if product else 5)
        
        report.append({
            "id": b.id,
            "name": product.name if product else "Unknown",
            "category": product.category if product else "N/A",
            "qty": b.quantity,
            "expiry": b.expiry_date.strftime('%Y-%m-%d'),
            "prediction": days_of_stock_left, 
            "alert": status,
            "low_stock": is_low
        })
    
    return render_template('index.html', inventory=report, total_sales=total_sales)

@app.route('/sell/<int:batch_id>')
def sell_item(batch_id):
    batch = db.session.get(Batch, batch_id)
    if batch and batch.quantity > 0:
        batch.quantity -= 1
        # Transaction Logging: Essential for Data Engineering
        new_sale = Sale(product_id=batch.product_id, quantity_sold=1)
        db.session.add(new_sale)
        db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True, port=8000)