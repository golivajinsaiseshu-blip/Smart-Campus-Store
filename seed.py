from app import app
from models import db, Product, Batch
from datetime import datetime, timedelta

def seed_data():
    with app.app_context():
        # 1. Clear existing data to start fresh
        db.drop_all()
        db.create_all()

        # 2. Create some Products
        p1 = Product(name="Amul Milk 500ml", category="Dairy", min_stock_level=10)
        p2 = Product(name="Classmate Notebook", category="Stationery", min_stock_level=20)
        p3 = Product(name="Lays Classic Chips", category="Snacks", min_stock_level=15)
        
        db.session.add_all([p1, p2, p3])
        db.session.commit() # Save products first to get their IDs

        # 3. Create Batches with different expiry dates
        today = datetime.now().date()
        
        # Batch 1: Expired (Red alert test)
        b1 = Batch(product_id=p1.id, quantity=5, expiry_date=today - timedelta(days=2))
        
        # Batch 2: Expiring in 4 days (Yellow alert test)
        b2 = Batch(product_id=p1.id, quantity=10, expiry_date=today + timedelta(days=4))
        
        # Batch 3: Fresh (Green alert test)
        b3 = Batch(product_id=p2.id, quantity=50, expiry_date=today + timedelta(days=200))

        db.session.add_all([b1, b2, b3])
        db.session.commit()
        
        print("✅ Database seeded with test items!")

if __name__ == "__main__":
    seed_data()