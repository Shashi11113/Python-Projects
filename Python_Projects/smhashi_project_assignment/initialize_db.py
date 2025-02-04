import sqlite3

# Database connection
def initialize_db():
    connection = sqlite3.connect("waamo.db")
    cursor = connection.cursor()

    # Create the menu table with the quantity column
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS menu_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                quantity TEXT DEFAULT 'Unlimited'  
            )
        ''')

    # Create the contacts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')

    # Prepopulate the menu with the provided items
    menu_items = [
        ("Hummus Dip", "A creamy dip made with chickpeas, tahini, lemon juice, and garlic.", 8.98, 'Unlimited'),
        ("Hilib", "Oven-roasted goat meat served with rice or bread.", 20.04, 'Unlimited'),
        ("Beef Sukhaar", "Stir-fried beef with spices, onions, and vegetables.", 18.81, 'Unlimited'),
        ("Chicken Sukhaar", "Stir-fried chicken with spices, onions, and vegetables.", 16.35, 'Unlimited'),
        ("Chicken Steak", "Grilled chicken steak marinated in spices.", 17.58, 'Unlimited'),
        ("Chicken Leg", "Juicy oven-roasted chicken leg seasoned with spices.", 15.12, 'Unlimited'),
        ("Beef Steak", "Grilled beef steak cooked to perfection.", 17.58, 'Unlimited'),
        ("Fish Fillet", "Pan-seared fish fillet with lemon and herbs.", 17.58, 'Unlimited'),
        ("Lamb Shank", "Slow-cooked lamb shank in a flavorful sauce.", 22.51, 'Unlimited'),
        ("Ethiopian Injera", "Traditional Ethiopian flatbread made with teff flour.", 15.12, 'Unlimited'),
        ("Chapatti Wrap", "Soft chapatti stuffed with vegetables or meat.", 10.20, 'Unlimited'),
        ("Soor", "Traditional Somali dish made of cornmeal and spices.", 18.81, 'Unlimited'),
        ("Sports Platter", "A platter of 2 items and 2 sides.", 31.13, 'Unlimited'),
        ("Soda", "Refreshing carbonated soft drink.", 1.60, 'Unlimited'),
        ("Tea", "Hot brewed tea with optional sugar.", 1.60, 'Unlimited'),
        ("Mango Juice", "Freshly blended mango juice.", 1.60, 'Unlimited'),
        ("Watermelon Juice", "Freshly blended watermelon juice.", 1.60, 'Unlimited'),
    ]

    # Insert menu items into the table
    cursor.executemany('''
        INSERT INTO menu_items (name, description, price, quantity) 
        VALUES (?, ?, ?, ?)
    ''', menu_items)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_db()

