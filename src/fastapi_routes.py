from fastapi import APIRouter
from pydantic import BaseModel
import nextcord_calls as nxc

router = APIRouter()

class SendShareRequest(BaseModel):
    url: str

@router.post("/send_shares")
def send_shares(req: SendShareRequest):
    delivered = nxc.send_share(req.url)
    return {
        "status": "delivered" if delivered else "queued",
        "url": req.url,
        "channel_id": nxc.CHANNEL_ID,
    }
