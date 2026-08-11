import sys

import fastapi as f
import uvicorn
from contextlib import asynccontextmanager

import fastapi_routes as fr
import nextcord_calls as nxc

@asynccontextmanager
async def lifespan(app):
    nxc.start_bot()
    yield

app = f.FastAPI(lifespan=lifespan)
app.include_router(fr.router)

if __name__ == "__main__":
    with open("token.txt", "r") as f:
        token = f.read().strip()
        if token == "INPUT_DISCORD_TOKEN_FOR_YOUR_CLANKER":
            print("rethink your life choices. (you forgot to put a discord bot token)")
            sys.exit(1)
        elif not token:
            print("token.txt is empty or not set (how tf)")
            sys.exit(1)
        else:
            print("valid. go ahead, cheif!")
            print(''.join('*' if char != '.' else '.' for char in token))
    uvicorn.run(app, host="0.0.0.0", port=8000)