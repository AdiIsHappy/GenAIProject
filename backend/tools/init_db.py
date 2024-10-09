# backend/tools/init_db.py

import pymongo

def initialize_database():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["company_db"]

    # Sample collections
    employees = db["employees"]
    projects = db["projects"]

    # Insert sample data
    employees.insert_many([
        {"name": "Alice", "role": "Engineer", "department": "Development"},
        {"name": "Bob", "role": "Designer", "department": "Design"},
        {"name": "Charlie", "role": "Manager", "department": "HR"}
    ])

    projects.insert_many([
        {"project_name": "Project Alpha", "status": "Ongoing", "owner": "Alice"},
        {"project_name": "Project Beta", "status": "Completed", "owner": "Bob"}
    ])

    # Interaction history
    history = db["history"]
    history.insert_one({"interaction": "Initial setup", "details": "Database initialized with sample data."})

    print("Database initialized with sample data.")

if __name__ == "__main__":
    initialize_database()
