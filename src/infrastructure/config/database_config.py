import os

class DatabaseConfig:
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')
    POOL_SIZE = int(os.getenv('DB_POOL_SIZE', 5))
