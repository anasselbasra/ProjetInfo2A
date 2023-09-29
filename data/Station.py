from data.Record import Record
from data.Location import Location
class Station:
    
    def __init__(self, station_id: int, station_name: str, loc: Location, history: list[Record]):
        self._stationId = station_id
        self._stationName = station_name
        self.__loc = loc
        self._history = []
        for record in history :
            if isinstance(record , Record):
                self._history += [record]
                    
    @property
    def getStationID(self) -> int:
        return self._stationId
            
    @property
    def getStationName(self) -> str:
        return self._stationName
    
    @property
    def getStationCoordinates(self) -> tuple[float]:
        return self.__loc.getLocation
    
    @property
    def getStationHistory(self) -> list[Record]:
        return self._history
    
    @property
    def getStationLon(self) -> float:
        return self.__loc.getLongitude
    
    @property
    def getStationLat(self) -> float:
        return self.__loc.getLatitude
    
    