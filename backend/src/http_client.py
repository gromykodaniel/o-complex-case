import aiohttp
from fastapi import HTTPException
class HTTPClient:
    async def get_coords(self ,  city):
        async with aiohttp.ClientSession() as session:
            url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"

            async with session.get(url) as response:
                data = await response.json()

                if 'results' not in  data :raise HTTPException(status_code=404)
                if city.lower() == data['results'][0]['name'].lower():
                    latitude = data["results"][0]["latitude"]
                    longitude = data["results"][0]["longitude"]

            url2 = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

            async with session.get(url2) as response:
                weather_data = await response.json()
                temperature = weather_data["current_weather"]["temperature"]
                windspeed = weather_data["current_weather"]["windspeed"]
                return {"temperature":temperature, "windspeed":windspeed}


