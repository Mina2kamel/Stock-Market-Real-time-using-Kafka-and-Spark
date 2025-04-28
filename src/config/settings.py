from dataclasses import dataclass
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

@dataclass
class Config:
    host: str = os.getenv("MYSQL_HOST")
    port: int = int(os.getenv("MYSQL_PORT"))
    user: str = os.getenv("MYSQL_USER")
    password: str = os.getenv("MYSQL_PASSWORD")
    database: str = os.getenv("MYSQL_DATABASE")

    API_KEY: str = os.getenv("ALPHA_VANTAGE_API_KEY")



# Global config instance
config = Config()
