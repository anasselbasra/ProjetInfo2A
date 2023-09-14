import sqlite3
from sqlite3 import Error

# Create the Station table
initialize_station_request = """CREATE TABLE IF NOT EXISTS Station (
    id INT PRIMARY KEY,
    nom TEXT,
    lon NUMERIC(10, 6),
    lat NUMERIC(10, 6)
);"""

# Create the Date table
initialize_date_request = """CREATE TABLE IF NOT EXISTS Date (
    id INT PRIMARY KEY,
    date_minute DATETIME
);"""

# Create the Record table
initialize_record_request = """CREATE TABLE IF NOT EXISTS Record (
    station_id INT,
    date_id INT,
    variation INT,
    FOREIGN KEY (station_id) REFERENCES Station(id),
    FOREIGN KEY (date_id) REFERENCES Date(id)
);"""

db_file = "project_database.db"

# Create connection to the main DB
def createConnection():
    try:
        conn=sqlite3.connect(db_file)
        print("Database created successfully")
        return conn
    except sqlite3.Error as e:
        print("Error while connecting to db",e)

# Create cursor to execute SQL commands
conn = createConnection()
cur = conn.cursor()

# Execute SQL commands to initialize DB and TABLES
try :
    print ("Creating tables...")
    cur.execute(initialize_station_request)
    cur.execute(initialize_date_request)
    cur.execute(initialize_record_request)
except Exception as error:
    print ('error', error)
else:
    print ("Tables created successfully")
finally:
    print ("Closing Connections ... ")
    
