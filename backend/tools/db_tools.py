from pymongo import MongoClient
import json
import os

# Setup and connection to MongoDB
def get_database():
    client = MongoClient('mongodb://localhost:27017/')
    return client['sample_supplies']

db = get_database()

def getToolsInfo():
    tools_file_path = os.path.join(os.path.abspath('.'),'tools', 'tools_info.json')
    with open(tools_file_path) as f:
        tools = f.readlines()
    return tools

# Transaction APIs
def get_transactions(filter_criteria={}):
    return list(db.sales.find(filter_criteria))

def post_transaction(transaction_data):
    return db.sales.insert_one(transaction_data).inserted_id

def update_transaction(transaction_id, update_data):
    return db.sales.update_one({'_id': transaction_id}, {'$set': update_data}).modified_count

def delete_transaction(transaction_id):
    return db.sales.delete_one({'_id': transaction_id}).deleted_count

# Analytics and Reporting APIs
def sales_summary():
    pipeline = [{"$group": {"_id": "$storeLocation", "totalSales": {"$sum": 1}}}]
    return list(db.sales.aggregate(pipeline))

def revenue_analysis():
    pipeline = [
        {"$unwind": "$items"},
        {"$group": {"_id": "$storeLocation", "totalRevenue": {"$sum": {"$multiply": ["$items.price", "$items.quantity"]}}}}
    ]
    return list(db.sales.aggregate(pipeline))

# Customer Management APIs
def get_customers(filter_criteria={}):
    return list(db.sales.find(filter_criteria, {"customer": 1}))

def update_customer_info(customer_email, update_data):
    return db.sales.update_many({'customer.email': customer_email}, {'$set': {'customer': update_data}}).modified_count

def customer_purchase_history(customer_email):
    return list(db.sales.find({"customer.email": customer_email}))

# Item Management APIs
def get_items():
    return list(db.sales.distinct("items"))

def update_item(item_name, update_data):
    return db.sales.update_many({"items.name": item_name}, {'$set': {"items.$": update_data}}).modified_count

# Store Management APIs
def list_stores():
    return list(db.sales.distinct("storeLocation"))

def store_performance():
    pipeline = [
        {"$group": {"_id": "$storeLocation", "totalSales": {"$sum": 1}, "averageSatisfaction": {"$avg": "$customer.satisfaction"}}}
    ]
    return list(db.sales.aggregate(pipeline))

# Coupon and Promotions APIs
def apply_coupon(transaction_id, coupon_code):
    discount = 0.1  # Assuming 10% discount for the coupon
    return db.sales.update_one({'_id': transaction_id}, {'$mul': {'items.$.price': (1 - discount)}}).modified_count

def create_manage_coupons(coupon_data):
    return db.coupons.insert_one(coupon_data).inserted_id

