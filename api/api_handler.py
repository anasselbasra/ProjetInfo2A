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
async def get_data():
    # Initialize an HTTP client
    async with httpx.AsyncClient() as client:
        try:
            # Send a GET request to the OpenDataSoft API
            response = await client.get(BASE_URL)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Return the JSON response from the API
                return response.json()
            else:
                # Handle error cases
                return {"error": f"Request failed with status code {response.status_code}"}
        except Exception as e:
            return {"error": str(e)}
        
if __name__ == "__main__":
    print("Starting server")
    uvicorn.run(app, host = "127.0.0.1", port = 8000)