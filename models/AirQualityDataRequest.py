
class AirQualityDataRequest:
    def __init__(self, city, state, country, api_key):
        self.city = city
        self.state = state
        self.country = country
        self.api_key = api_key
        self.data = None

    def __str__(self):
        if self.data:
            return str(self.data)
        return "No data available."
