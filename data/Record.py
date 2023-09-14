from datetime import datetime
class Record:

    def __init__(self, timestamp: datetime, availablebikes: int):
        if availablebikes < 0:
            raise ValueError("Number of bikes available cannot be negative !")
        else:
            self.timestamp = timestamp
            self.availablebikes = availablebikes