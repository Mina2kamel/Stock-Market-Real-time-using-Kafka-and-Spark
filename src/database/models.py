from sqlalchemy import Column, String, Float, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy ORM base class
Base = declarative_base()

class StockModel(Base):
    """
    ORM model for intraday stock data with composite primary key.
    """
    __tablename__ = 'stock_intraday'

    timestamp = Column(DateTime, primary_key=True, index=True)
    symbol = Column(String(10), nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<StockModel(symbol={self.symbol}, timestamp={self.timestamp})>"
