from config import config
from database import MySQLHandler, StockModel
from api import AlphaVantageAPI
from utils import logger


def main():

    # Initialize API and DB manager
    api = AlphaVantageAPI(config.API_KEY)
    db_handler = MySQLHandler()

    # Fetch stock data
    records = api.get_intraday_stock_data(symbol='IBM')

    try:
        db_handler.batch_merge(records=records, model=StockModel)
    except Exception as e:
        logger.error(f"Failed to insert records: {e}")

if __name__ == "__main__":
    main()
