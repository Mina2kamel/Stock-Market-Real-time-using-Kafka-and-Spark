import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config
from contextlib import contextmanager

logger = logging.getLogger(__name__)

class MySQLManager:
    _instance = None
    _engine = None
    _SessionFactory = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._setup_engine()
        return cls._instance

    def _setup_engine(self):
        if not MySQLManager._engine:
            try:
                mysql_url = (
                    f"mysql+mysqlconnector://{config.user}:{config.password}"
                    f"@{config.host}:{config.port}/{config.database}"
                )
                MySQLManager._engine = create_engine(mysql_url, echo=False)
                MySQLManager._SessionFactory = sessionmaker(bind=MySQLManager._engine)
                logger.info("SQLAlchemy engine created successfully.")
            except Exception as e:
                logger.error(f"Error creating SQLAlchemy engine: {e}")
                raise

    @contextmanager
    def session(self):
        """Context manager for database session."""
        session = self._SessionFactory()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error(f"Session rollback because of: {e}")
            raise
        finally:
            session.close()
            logger.info("Session closed.")

    def dispose_engine(self):
        """Dispose the SQLAlchemy engine."""
        if MySQLManager._engine:
            MySQLManager._engine.dispose()
            logger.info("Engine disposed.")
