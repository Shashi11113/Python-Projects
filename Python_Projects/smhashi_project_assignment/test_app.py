import pytest
import os
import sqlite3
from app import app  # Import the Flask app
from db_helpers import cleanup_test_data


# Setup for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['DATABASE'] = 'waamo.db'  # Use the actual waamo.db for testing

    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def set_testing_env():
    os.environ['FLASK_ENV'] = 'testing'  # Set Flask to use the testing environment
    yield
    del os.environ['FLASK_ENV']  # Clean up after tests


# Test Routes
def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Waamo Restaurant" in response.data

def test_history_route(client):
    response = client.get('/history')
    assert response.status_code == 200
    assert b"Our History" in response.data


def test_menu_route(client):
    response = client.get('/menu')
    assert response.status_code == 200
    assert b"Our Delicious Menu" in response.data


def test_location_route(client):
    response = client.get('/location')
    assert response.status_code == 200
    assert b"Our Location" in response.data


def test_contact_route(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b"Contact Us" in response.data


# Test Form Submissions
def test_contact_form_submission(client):
    response = client.post('/contact', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'message': 'This is a test message.'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Thank you for your message" in response.data


# Test Database Operations
def test_database_entry(client):
    # Check if the contact form submission stores data in the database
    connection = sqlite3.connect('waamo.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name = ?", ('Test User',))
    result = cursor.fetchone()
    connection.close()
    assert result is not None
    assert result[1] == 'Test User'
    assert result[2] == 'test@example.com'
    cleanup_test_data()


# Test Search Functionality
def test_menu_search(client):
    # Simulate adding menu items in the database
    with app.app_context():
        connection = sqlite3.connect('waamo.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO menu_items (name, description, price) VALUES (?, ?, ?)",
                       ('Borito', 'Delicious meat stuffed flatbread', 17.99))
        connection.commit()
        connection.close()

    # Perform search
    response = client.get('/menu?search=Borito')
    assert response.status_code == 200
    assert b"Borito" in response.data
    cleanup_test_data()

cleanup_test_data()

# Test Static Pages and CSS
def test_static_files(client):
    response = client.get('/static/css/style.css')
    assert response.status_code == 200
    assert b"body" in response.data  # Ensure CSS is loaded

