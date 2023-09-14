from fastapi import FastAPI
import httpx

app = FastAPI()

# Define the base URL for the OpenDataSoft API
BASE_URL = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/json"

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
