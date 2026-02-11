# Smart-Campus-Store 
"Intelligent Inventory, Zero Wastage"

##Reference: Problem Statement 2.4  Smart Campus Store Inventory & Expiry Tracker.

##FEATURES:
Feature 1: 📦 Intelligent Item Catalog: Management of 50+ unique items across multiple categories (Stationery, Snacks, Dairy, etc.).

Feature 2: Dynamic, color-coded alerts based on shelf life:

🔴 EXPIRED (Past date)

🟠 CRITICAL (Within 7 days)

🟡 WARNING (Within 15 days)

🟢 FRESH (Safe to sell)

Feature 3: A "Smart" analytics engine that calculates Estimated Days Left for each product based on real-time consumption data.

##Tech Stack:
Frontend: HTML5, CSS3, Bootstrap 5, and Jinja2 Templating
Database: SQLite with SQLAlchemy ORM (Batch and Transaction tracking)
Backend: Python 3.14 with Flask Framework

##Installation:
1. Clone the Repository
   git clone <your-github-link-here>
cd smart-campus-store
2. Install Dependencies like
    Flask==3.0.0
    Flask-SQLAlchemy==3.1.1
   
5. Initialize the Database
This will create the inventory_v2.db file and all necessary tables (Product, Batch, Sale).
python app.py

7. Seed Required Data
Execute the seeder script to populate the catalog with the required 50+ items.
python bulk_data.py

9. Launch the Dashboard
Run the server and visit http://127.0.0.1:8000/ in your browser.
python app.py

Logic Behind:
Our system utilizes a Transactional Data Pipeline. Rather than just updating a counter, every "Sell" action generates a new record in the Sale table. The Predictive Logic then processes this historical data using

##Team Monarch
G.Vajin Sai Seshu 
G.Nehal Sai Krishna
V.B.Sai Akhilesh


