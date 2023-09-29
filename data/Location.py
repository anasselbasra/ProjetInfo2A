class Location():
    
    def __init__(self, lon: float = 0, lat: float = 0):
        
        if (abs(lat)>90 or abs(lon)>180):
            raise ValueError("Invalid coordinates")
        
        if(not(isinstance(lat, float) and isinstance(lon, float))):
            raise TypeError("Both arguments must be float type")
        
        self.lon = lon
        self.lat = lat
    
    @property
    def getLocation(self):
        return (self.lat, self.lon)
    
    @property
    def getLatitude(self):
        return self.lat
    
    @property
    def getLongitude(self):
        return self.lon
