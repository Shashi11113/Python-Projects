from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import sqlite3
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Secret key for sessions
app.secret_key = os.environ.get(
    '5c85345e7343a523c5e4bd7fb5187a80e82ef75daac62bc3',
    '574e896da41e4a6e3f5b0d8e4b98fa50521c4678b1995ad8'
)

# Home Route (redirects to /menu)
@app.route('/')
def home():
    return render_template('home.html')

def get_menu_items(keyword=None):
    connection = sqlite3.connect("waamo.db")
    cursor = connection.cursor()

    # Modify the query to filter based on the search keyword
    if keyword:
        cursor.execute("SELECT * FROM menu_items WHERE name LIKE ?", ('%' + keyword + '%',))
    else:
        cursor.execute("SELECT * FROM menu_items")

    products = cursor.fetchall()
    connection.close()
    return products


@app.route('/menu', methods=['GET'])
def menu():
    keyword = request.args.get('search')  # Get the search keyword from the request
    filtered_item = None

    # Get all products from the database based on the search query
    if keyword:
        products = get_menu_items(keyword)  # Fetch filtered products based on search term
    else:
        products = get_menu_items()  # Fetch all products if no search term is provided

    # Hard-code the images based on the item name (no 'images/' here)
    image_paths = {
        'hummus dip': 'hummus.jpeg',
        'beef sukhaar': 'beef_sukhaar.jpg',
        'beef steak': 'beef_steak.jpeg',
        'chapatti wrap': 'chapatti_wrap.jpeg',
        'chicken leg': 'chicken_leg.jpeg',
        'hilib': 'hilib.jpeg',
        'chicken steak': 'chicken_steak.jpg',
        'chicken sukhaar': 'chicken_sukhaar.jpg',
        'ethiopian injera': 'ethiopian_injera.jpeg',
        'fish fillet': 'fish_fillet.jpeg',
        'history': 'history.jpg',
        'lamb shank': 'lamb_shank.jpeg',
        'mango juice': 'mango_juice.jpeg',
        'soda': 'soda.jpeg',
        'soor': 'soor.jpeg',
        'sports platter': 'sports_platter.jpeg',
        'tea': 'tea.jpeg',
        'waamo history': 'waamo_history.jpg',
        'watermelon juice': 'watermelon_juice.jpeg'
    }

    # Normalize item names and assign image paths
    product_dicts = []
    for item in products:
        # Convert tuple to dictionary
        item_name_normalized = item[1].strip().lower()  # Normalize name (lowercase + strip spaces)
        item_dict = {
            'name': item[1],  # Assuming item[1] is the name of the item
            'description': item[2],  # Assuming item[2] is the description
            'price': item[3],  # Assuming item[3] is the price
            'quantity': 'Unlimited',  # Assuming item[4] is the quantity
            'image': image_paths.get(item_name_normalized, None)  # Get image path (case-insensitive, stripped)
        }

        # If the image path is missing, assign a default image
        if not item_dict['image']:
            item_dict['image'] = 'default.jpg'  # Use 'default.jpg' without 'images/'

        product_dicts.append(item_dict)

    # Filter the products to find the matching item (if search term is provided)
    for item in product_dicts:
        if keyword and keyword.lower() in item['name'].lower():
            filtered_item = item
            break

    # If filtered_item is None, set its image to 'default.jpg'
    if filtered_item and not filtered_item.get('image'):
        filtered_item['image'] = 'default.jpg'



    return render_template('menu.html', item=filtered_item, products=product_dicts, keyword=keyword)

# History Route
@app.route('/history')
def history():
    return render_template('history.html')

# Location Route
@app.route('/location')
def location():
    return render_template('location.html')

# Contact Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Store the message in the database
        store_message_in_db(name, email, message)

        # Return an alert thanking the user
        return '''
            <script>
                alert("Thank you for your message! We will respond to the best of our ability.");
                window.location.href = '/contact';  // Refresh the page
            </script>
        '''
    return render_template('contact.html')

# Helper function to store messages in the database
def store_message_in_db(name, email, message):
    connection = sqlite3.connect("waamo.db")
    cursor = connection.cursor()

    # Create the contacts table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT
        )
    ''')

    # Insert the contact message
    cursor.execute('''
        INSERT INTO contacts (name, email, message) 
        VALUES (?, ?, ?)
    ''', (name, email, message))

    connection.commit()
    connection.close()

if __name__ == '__main__':
    app.run(debug=True)


