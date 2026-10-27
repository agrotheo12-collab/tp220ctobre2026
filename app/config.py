import os

from dotenv import load_dotenv

load_dotenv()  # lit le fichier .env en local ; dans Docker, les variables viennent de Compose

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "annonces_db")