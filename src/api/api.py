import requests
import logging

logger = logging.getLogger(__name__)

class AlphaVantageAPI:
    BASE_URL = "https://www.alphavantage.co/query"

    def __init__(self, api_key: str, interval: str = "1min"):
        self.api_key = api_key
        self.interval = interval

    def get_intraday_stock_data(self, symbol: str):
        """
        Fetch intraday time series data with timestamp.

        Parameters:
            symbol (str): Stock symbol (e.g. 'IBM')

        Returns:
            list[dict]: List of intraday stock data with timestamps
        """
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': self.interval,
            'apikey': self.api_key
        }

        try:
            response = requests.get(self.BASE_URL, params=params)
            data = response.json()
            key = f'Time Series ({self.interval})'
            time_series = data[key]

            records = [
                {
                    'symbol': symbol.upper(),
                    'timestamp': timestamp,
                    'open': float(values['1. open']),
                    'high': float(values['2. high']),
                    'low': float(values['3. low']),
                    'close': float(values['4. close']),
                    'volume': int(values['5. volume']),
                }
                for timestamp, values in time_series.items()
            ]
            logger.info(f"Fetched {len(records)} records for symbol: {symbol.upper()}")
            return records

        except KeyError:
            logger.error("Invalid API response or rate limit exceeded.")
            raise ValueError("Invalid API response or rate limit exceeded.")
        except Exception as e:
            logger.error(f"Error fetching data: {e}")
            raise ConnectionError(f"Error fetching data: {e}")
