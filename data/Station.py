from data.Record import Record
class Station:
    
    def __init__(self, station_id: int, station_name: str, lon: float, lat: float, history: list[Record]) -> Station:
        self._stationId = station_id
        self._stationName = station_name
        self.__lon = lon
        self.__lat = lat
        self._history = []
        for record in history :
            if isinstance(record , Record):
                self._history += [record]
                    
                    
    @property
    def getStationID() -> int:
        return self._stationId
            
    @property
    def getStationName() -> str:
        return self._stationName
    
    @property
    def getStationCoordinates() -> tuple[float]:
        return (self.__lon, self.__lat)
    
    @property
    def getStationHistory() -> list[Record]:
        return self._history