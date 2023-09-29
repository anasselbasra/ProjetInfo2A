from datetime import datetime

class Date:
    
    def __init__(self, date: datetime):
        self.date = date
    
    @property
    def getDate(self) -> Date:
        return self.date
    
    @property
    def isSuperior(self, date2: Date) -> bool:
        return (self.date >= date2)
    
    @property
    def isInferior(self, date2: Date) -> bool:
        return (self.date <= date2)
    