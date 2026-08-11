import asyncio
import threading
from datetime import datetime

import nextcord as nc

CHANNEL_ID = 1536665454108614709

client = None
bot_loop = None
_pending = []

def send_share(url):
    if bot_loop is None:
        _pending.append(url)
        print("Bot not ready yet; queued command")
        return False
    asyncio.run_coroutine_threadsafe(post_share(url), bot_loop)
    return True

async def post_share(url):
    embed = nc.Embed(
        title="A pending new share..",
        description=f"""———————————————————————————————————
{url}
———————————————————————————————————
Please review it, and approve or deny it by clicking the reaction below.
If you are not a developer, please avoid those buttons.""",
        color=nc.Color(0xdd2ef4),
    )
    embed.set_footer(text=f"Posted at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} as GMT+8")

    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print(f"Couldn't find channel {CHANNEL_ID}")
        return
    await channel.send(embed=embed)
    print(f"Sent to channel {CHANNEL_ID}: {url}")

def start_bot():
    global client, bot_loop

    with open("token.txt", "r") as f:
        token = f.read().strip()

    client = nc.Client()

    @client.event
    async def on_ready():
        global bot_loop
        bot_loop = asyncio.get_running_loop()
        while _pending:
            url = _pending.pop(0)
            await post_share(url)
        print(f"Logged in as {client.user}")

    threading.Thread(target=lambda: asyncio.run(client.start(token)), daemon=True).start()

if __name__ == "__main__":
    start_bot()
