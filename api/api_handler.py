# Import necessary modules
import requests
from fastapi import FastAPI, Request
import uvicorn
import json
import httpx

# Creating API
app = FastAPI()

# Base URL for the app
BASE_URL= "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/json"

@app.get("/")
async def getAvailableStations():
    # Initialize an HTTP client
    async with httpx.AsyncClient() as client:
        try:
            # Send a GET request to the OpenDataSoft API
            response = await client.get(BASE_URL)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Return the JSON response from the API 
                data = response.json()
                velib_data = []
                
                for records in data:
                    station_id=records['stationcode']
                    station_name=records['name']
                    lat=float((records['coordonnees_geo']['lat']))
                    lon=float((records['coordonnees_geo']['lon']))
                    numbikes=int((records['numbikesavailable']))
                    new_record={
                        'station': {
                            'name':station_name,
                            'uuid':station_id,
                            'latitude':lat,
                            'longitude':lon,
                            'numbikesavailable':numbikes},
                        }
                    if numbikes > 0:
                        velib_data.append({**new_record})
                    
                return {'velibs':velib_data}
                
            else:
                # Handle error cases
                return {"error": f"Request failed with status code {response.status_code}"}
        except Exception as e:
            return {"error": str(e)}
        
        

        
if __name__ == "__main__":
    print("Starting server")
    uvicorn.run(app, host = "127.0.0.1", port = 8000)