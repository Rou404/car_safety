import requests
import sqlite3


# Function to fetch data from NHTSA API
def fetch_nhtsa_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return None


def create_database():
    # Connect to SQLite database (create it if it doesn't exist)
    conn = sqlite3.connect('vehicle_data.db')
    cursor = conn.cursor()

    # Create a table to store vehicle data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_year TEXT,
            make TEXT,
            model TEXT,
            vehicle_description TEXT,
            vehicle_id TEXT
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

create_database()

def insert_data(model_year, make, model, vehicle_description, vehicle_id):
    # Connect to SQLite database
    conn = sqlite3.connect('vehicle_data.db')
    cursor = conn.cursor()

    # Insert data into the 'vehicles' table
    cursor.execute('''
        INSERT INTO vehicles (model_year, make, model, vehicle_description, vehicle_id)
        VALUES (?, ?, ?, ?, ?)
    ''', (model_year, make, model, vehicle_description, vehicle_id))

    # Commit changes and close the connection
    conn.commit()
    conn.close()


def crawl_nhtsa_data(start_year, end_year):
    base_url = "https://api.nhtsa.gov/SafetyRatings/modelyear"

    for model_year in range(start_year, end_year + 1):
        model_year_data = fetch_nhtsa_data(f"{base_url}/{model_year}")
        for make_entry in model_year_data.get('Results', []):
            make = make_entry.get('Make', '')
            make_url = f"{base_url}/{model_year}/make/{make}"
            make_data = fetch_nhtsa_data(make_url)
            if make_data:
                for model_entry in make_data.get('Results', []):
                    model = model_entry.get('Model', '')
                    model_url = f"{base_url}/{model_year}/make/{make}/model/{model}"

                    model_data = fetch_nhtsa_data(model_url)

                    if model_data:
                        for vehicle_entry in model_data.get('Results', []):
                            vehicle_description = vehicle_entry.get('VehicleDescription', '')
                            vehicle_id = vehicle_entry.get('VehicleId', '')
                            insert_data(model_year, make, model, vehicle_description, vehicle_id)
                            print(model_year, make, model, vehicle_description, vehicle_id)
# Run the main function for a range of years
crawl_nhtsa_data(2021, 2024)
