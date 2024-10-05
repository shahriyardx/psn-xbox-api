import asyncio

from hypercorn import Config
from hypercorn.asyncio import serve

from src import app
from utils.env import env

config = Config()
config.bind = f"{env.HOST}:{env.PORT}"
config.use_reloader = True

asyncio.run(serve(app, config))
