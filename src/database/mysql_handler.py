
import logging
from .mysql_manager import MySQLManager
from .models import Base

# import the logger
logger = logging.getLogger(__name__)

class MySQLHandler:
    def __init__(self):
        """Initialize with a MySQLManager instance."""
        self.db_manager = MySQLManager()
        self.create_tables()

    def create_tables(self):
        """Ensure that all tables defined in models are created."""
        try:
            # Create tables if they do not exist
            Base.metadata.create_all(self.db_manager._engine)
            logger.info("Tables created successfully or already exist.")
        except Exception as e:
            logger.error(f"Error creating tables: {e}")
            raise

    def batch_merge(self, records, model, batch_size=100):
        """Merge records in batches to avoid single record merges."""
        try:
            with self.db_manager.session() as session:
                # Split the records into smaller chunks
                for i in range(0, len(records), batch_size):
                    batch = records[i:i+batch_size]
                    
                    # Merge each batch of records
                    for record in batch:
                        obj = model(**record)
                        session.merge(obj)

                    logger.info(f"{len(batch)} records merged successfully (batch {i // batch_size + 1}).")
        
        except Exception as e:
            logger.error(f"Error during batch merge: {e}")
            raise
