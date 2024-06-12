from typing import Dict, Any


class AirQualityResponse:
    def __init__(self, status: str, data: Dict[str, Any]):
        self.status = status
        self.city = data['city']
        self.state = data['state']
        self.country = data['country']
        self.locationType = data['location']['type']
        self.coordinates = data['location']['coordinates']
        self.pollutionTs = data['current']['pollution']['ts']
        self.pollutionAqicn = data['current']['pollution']['aqicn']
        self.weatherTs = data['current']['weather']['ts']
        self.weatherHu = data['current']['weather']['hu']
