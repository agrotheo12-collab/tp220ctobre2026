from contextlib import asynccontextmanager

from fastapi import FastAPI
from pymongo import ASCENDING, DESCENDING, AsyncMongoClient

from app import config

# Un seul client pour toute l'application : il gère lui-même un pool de connexions.
# tz_aware=True : les dates relues depuis MongoDB gardent leur fuseau (UTC).
mongo_client = AsyncMongoClient(config.MONGO_URL, tz_aware=True)
db = mongo_client[config.MONGO_DB]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Au démarrage : on crée les index (sans effet s'ils existent déjà).
    await db.annonces.create_index([("categorie", ASCENDING), ("created_at", DESCENDING)])
    yield
    # À l'arrêt : on ferme proprement les connexions.
    await mongo_client.close() 