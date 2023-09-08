import sqlite3

# Create or use an existing database
initialize_db_request = """CREATE DATABASE IF NOT EXISTS Velib_Application;
USE Velib_Application;"""

# Create the Station table
initialize_station_request = """CREATE TABLE IF NOT EXISTS Station (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50),
    lon NUMERIC(10, 6),
    lat NUMERIC(10, 6)
);"""

# Create the Date table
initialize_date_request = """CREATE TABLE IF NOT EXISTS Date (
    id INT PRIMARY KEY AUTO_INCREMENT,
    date_minute DATETIME,
    date_jour AS (CONVERT(varchar(255), date, 23))
);"""

# Create the Record table
initialize_record_request = """CREATE TABLE IF NOT EXISTS Record (
    station_id INT,
    date_id INT,
    variation INT,
    FOREIGN KEY (station_id) REFERENCES Station(id),
    FOREIGN KEY (date_id) REFERENCES Date(id)
);"""

# Create connection to the main DB
def createConnection():
    try:
        conn=sqlite3.connect('Velib_Database')
        return conn
    except sqlite3.Error as e:
        print("Error while connecting to db",e)
        conn = createConnection()
        

# Create cursor to execute SQL commands
conn = createConnection()
cur = conn.cursor()

# Execute SQL commands to initialize DB and TABLES
try :
    print ("Creating tables...")
    cur.execute(initialize_db_request)
    cur.execute(initialize_station_request)
    cur.execute(initialize_date_request)
    cur.execute(initialize_record_request)
except Exception as error:
    print ('error', error)
else:
    print ("Tables created successfully")
finally:
    print ("Closing Connections ... ")
    
