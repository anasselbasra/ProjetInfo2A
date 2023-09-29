from data.Date import Date
from datetime import datetime
class Record:

    def __init__(self, timestamp: Date, availablebikes: int):
        if availablebikes < 0:
            raise ValueError("Number of bikes available cannot be negative !")
        if timestamp > datetime.now():
            raise ValueError("Datetime can't be in the future !")
        else:
            self._timestamp = timestamp
            self._availablebikes = availablebikes
            
    @property
    def getAvailablebikes(self) -> int:
        return self._availablebikes
    
    @property
    def getTimestamp(self) -> Date:
        return self._timestamp
    
    