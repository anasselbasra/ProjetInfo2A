import sqlite3
from sqlite3 import Error
from utils.singleton import Singleton

class Database(metaclass=Singleton):  
    
    def __init__(self, db_file:str = "project_database.db"):
        self.__connection = sqlite3.connect(db_file)
    
    # Create connection to the main DB
    def getConnection(self):
        return self.__connection

    def initializeTables():
        # Create the Station table
        initialize_station_request = """CREATE TABLE IF NOT EXISTS Station (
            uuid INT PRIMARY KEY,
            nom TEXT,
            lon NUMERIC(10, 6),
            lat NUMERIC(10, 6)
        );"""

        # Create the Date table
        initialize_date_request = """CREATE TABLE IF NOT EXISTS Date (
            uuid INT PRIMARY KEY,
            date_minute DATETIME
        );"""

        # Create the Record table
        initialize_record_request = """CREATE TABLE IF NOT EXISTS Record (
            station_uuid INT,
            date_uuid INT,
            variation INT,
            FOREIGN KEY (station_id) REFERENCES Station(id),
            FOREIGN KEY (date_id) REFERENCES Date(id)
        );"""

        # Create cursor to execute SQL commands
        conn = self.getConnection()
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
    
