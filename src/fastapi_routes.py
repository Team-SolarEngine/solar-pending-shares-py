from fastapi import APIRouter
from pydantic import BaseModel
import nextcord_calls as nxc

router = APIRouter()

class SendShareRequest(BaseModel):
    url: str

@router.post("/send_shares")
def send_shares(req: SendShareRequest):
    """
    Sends a share to the bot, queuing it if the bot is not ready yet.

    Headers for web:
        "url" (str): The URL of the share to send. Must be a valid GitHub URL.

    Returns:
        status (str): The status of the share, either "delivered" or "queued".
        url (str): The URL of the share.
        channel_id (int): The ID of the channel the share was sent to.
    """

    delivered = nxc.send_share(req.url)
    return {
        "status": "delivered" if delivered else "queued",
        "url": req.url,
        "channel_id": nxc.CHANNEL_ID,
    }
