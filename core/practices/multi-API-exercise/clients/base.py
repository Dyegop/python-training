import requests
from datetime import timedelta



class RequestsManager:
    """Manage requests"""
    def __init__(self, url_base: str, url_suffix: str):
        self.url_base = url_base
        self.url_suffix = url_suffix
        self.end_point = url_base + url_suffix

    def __str__(self):
        return self.end_point

    def get(self):
        try:
            re = requests.get(self.end_point)
            re.raise_for_status()
            return re
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    @property
    def text(self):
        return self.get().text

    @property
    def json(self):
        return self.get().json()

    @staticmethod
    def daterange(start_date, end_date):
        """Auxiliar function to get dates in a range with format %Y-%m-%d"""
        for n in range(int((end_date - start_date).days)):
            yield (start_date + timedelta(n)).strftime("%Y-%m-%d")
