import pandas as pd

from .base import RequestsManager


class OpenExchangeClient(RequestsManager):
    """Class to manage open exchange api"""

    def __init__(self, url_base: str, url_suffix: str):
        super().__init__(url_base, url_suffix)

    def convert(self, p_from_amount, p_from_currency, p_to_currency):
        """Convert currencies"""
        rates = self.json["rates"]
        to_rate = rates[p_to_currency]
        if p_from_currency == "USD":
            return p_from_amount * to_rate
        else:
            from_in_usd = p_from_amount / rates[p_from_currency]
            return from_in_usd * to_rate

    def displot(self):
        """Save data for currencies exchange rates to dataframe"""
        rates = self.json["rates"]
        data = [v for k, v in rates.items()]
        index = [k for k, v in rates.items()]
        df = pd.DataFrame(data, index)
        print(df.head())
