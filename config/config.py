import os

class Config:
    API_VERSION = os.getenv("API_VERSION", "v1")
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
