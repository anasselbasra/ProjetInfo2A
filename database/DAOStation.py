from database.init_db import Database
from rare.utils.singleton import SingleInstance
from data.Station import Station
import sqlite3

class DAOStation(metaclass=SingleInstance):
    
    # Create method to create a new Station in the database
    def addNewStation(self, station: Station) -> bool:
        
        created = False
        
        with Database.getConnection as connection:
            cursor = connection.cursor()
            sqlAddStation = """INSERT INTO Station (stationid, stationname, lon, lat)
                            VALUES (%(uuid)s, %(name)s, %(lon)s, %(lat)s)"""
            cursor.execute(sqlAddStation, {"uuid": station.getStationID,
                                    "name": station.getStationName,
                                    "lon": station.getStationLon,
                                    "lat": station.getStationLat})
            res = cursor.fetchone()
        if res:
            return not(created)
        return created
        
    # Get method to retrieve Station by it's UUID
    def getStationByUUID(uuid: int) -> str:
        
        with Database.getConnection as connection:
            cursor = connection.cursor()
            sqlGetStation = "SELECT nom FROM Station WHERE uuid = %(uuid)s"
            cursor.execute(sqlGetStation, {"uuid": uuid})
            res = cursor.fetchone()
        if res:
            station_name = res['nom']
            return station_name
        return f"unable to find a station name with UUID = {uuid}"
