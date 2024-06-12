import requests

from models.AirQualityResponse import AirQualityResponse


class AirQualityService:
    BASE_URL = "https://api.airvisual.com/v2/city"

    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_air_quality_data(self, city, state, country):
        url = f"{self.BASE_URL}?city={city}&state={state}&country={country}&key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            response=response.json()
            air_quality_response = AirQualityResponse(response['status'], response['data'])
            return air_quality_response
        else:
            response.raise_for_status()
