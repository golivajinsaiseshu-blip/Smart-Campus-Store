from app import app
from models import db, Product, Batch
from datetime import datetime, timedelta
import random

def seed_bulk():
    with app.app_context():
        # WARNING: This deletes current data to start fresh with 50+ items
        db.drop_all()
        db.create_all()

        categories = ["Stationery", "Mess/Dairy", "Snacks", "Beverages", "Bookshop"]
        item_names = [
            "Pen", "Notebook", "Milk", "Bread", "Chips", "Marker", "Eraser", 
            "Juice", "A4 Paper", "Pencil", "Glue", "Chocolate", "Calculator"
        ]

        # Generate 54 items to exceed the 50-item requirement
        for i in range(1, 55):
            name = f"{random.choice(item_names)} {i}"
            cat = random.choice(categories)
            
            # Create Product with a random reorder/min stock level
            p = Product(name=name, category=cat, min_stock_level=random.randint(5, 15))
            db.session.add(p)
            db.session.commit() # Save product to get ID

            # Create random expiry: mix of expired, critical, and fresh
            random_days = random.randint(-5, 40)
            expiry = datetime.now().date() + timedelta(days=random_days)
            
            # Create Batch with random quantity (some will trigger Low Stock alert)
            b = Batch(product_id=p.id, quantity=random.randint(1, 60), expiry_date=expiry)
            db.session.add(b)

        db.session.commit()
        print("✅ Success! 54 items added to the database.")

if __name__ == "__main__":
    seed_bulk()