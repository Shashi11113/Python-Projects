# Sadam Hashi, CIS 345, 1:30pm to 2:45pm, A2

import sqlite3

# Creating the database and tables
db_name = "smhashi_companyDB.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

# Creating Contacts table
cursor.execute('''CREATE TABLE IF NOT EXISTS Contacts (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    Message TEXT
)''')

# Creating Products table
cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName TEXT NOT NULL,
    ProductDescription TEXT NOT NULL,
    Price REAL NOT NULL,
    QuantityAvailable INTEGER NOT NULL
)''')

# Commit changes after table creation
connection.commit()

# Adding values to the Contacts table
contacts_data = [
    ("Wendy", "Watson", "wendy.watson@example.com", "Interested in large discounts for bulk purchases."),
    ("James", "Scott", "james.scott@example.com", "Need details about your delivery process."),
    ("Sandra", "Brown", "sandra.brown@example.com", "Requesting a catalog for kitchen appliances."),
    ("Juliet", "Smith", "juliet.smith@example.com", "Inquiry about laptop warranties."),
    ("Alan", "Johnson", "alan.j@example.com", "Request for product catalog.")
]
cursor.executemany('''INSERT INTO Contacts (FirstName, LastName, Email, Message)
                       VALUES (?, ?, ?, ?)''', contacts_data)

# Adding values to the Products table
products_data = [
    ("Refrigerator Deluxe", "Energy-efficient refrigerator with smart controls", 999.99, 20),
    ("Washing Machine Pro", "Front-load washer with multiple wash cycles", 749.50, 15),
    ("Microwave Oven Plus", "Compact microwave with convection cooking", 129.99, 40),
    ("Air Conditioner Max", "Split AC with inverter technology", 599.99, 10),
    ("Vacuum Cleaner Pro", "Cordless vacuum with powerful suction", 199.99, 30),
    ("Dishwasher Elite", "High-capacity dishwasher with smart sensors", 869.99, 12),
    ("Ceiling Fan Modern", "Energy-efficient fan with remote control", 89.99, 50),
    ("Electric Kettle", "Fast-boiling kettle with auto shut-off", 49.99, 60),
    ("Blender Supreme", "High-performance blender for smoothies and soups", 189.99, 25),
    ("Toaster Premium", "4-slice toaster with customizable settings", 49.99, 35)
]
cursor.executemany('''INSERT INTO Products (ProductName, ProductDescription, Price, QuantityAvailable)
                       VALUES (?, ?, ?, ?)''', products_data)

# Commit changes and close the connection
connection.commit()
connection.close()

print(f"Database '{db_name}' created and populated successfully.")
