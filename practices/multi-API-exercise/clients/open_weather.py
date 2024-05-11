from .base import RequestsManager


class OpenWeatherClient(RequestsManager):
    """Class to manage open weather api"""

    def __init__(self, url_base: str, url_suffix: str):
        super().__init__(url_base, url_suffix)

    def forecast(self, loc):
        """Get forescast"""
        data = self.json
        weather = dict(data.get("weather")[0])
        # Get results
        print()
        print("Current weather in %s:" % loc)
        print(f"{weather['main']} - {weather['description']}")
        print("Temperature: %.1fºC" % (float(data["main"]["temp"]) - 273.15))
        print("Feels like: %.1fºC" % (float(data["main"]["feels_like"]) - 273.15))
        print(f"Pressure: {data['main']['pressure']}\n")
