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
    uvicorn.run(app, host="0.0.0.0", port=8000)