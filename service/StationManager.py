from data.Station import Station
from data.Location import Location
from database.DAOStation import DAOStation
from api.api_handler import getAvailableStations
from vincenty import vincenty

class StationManager():
    
    def getNearestStation(loc: Location) -> Station:
        
        stations = getAvailableStations()
        
        distance = []
        
        for station in stations["velibs"]:
            
            dist = vincenty(loc, (station["coordonnees_geo"]["lon"],station["coordonnees_geo"]["lat"]))
            distance.append((dist, station["uuid"]))
            