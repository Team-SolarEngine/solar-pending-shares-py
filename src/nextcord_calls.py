import asyncio
import threading
from datetime import datetime
import git_stuff as gs

import nextcord as nc

CHANNEL_ID = 1536665454108614709

client = None
bot_loop = None
_pending = []

lists_of_approved_people = [
    1149685116042485781, # daveberry
    978699497876103199, # videobot
    714247788715573310, # char
]

def build_embed(title, description):
    embed = nc.Embed(
        title=title,
        description=description,
        color=nc.Color(0xdd2ef4),
    )
    embed.set_footer(text=f"Posted at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} as GMT+8")
    return embed

class Shares_Buttons(nc.ui.View):
    def __init__(self, channel, url):
        super().__init__()
        self.channel = channel
        self.url = url

    @nc.ui.button(label="Approve", emoji="✅")
    async def approve(self, button: nc.ui.Button, interaction: nc.Interaction):
        if interaction.user.id not in lists_of_approved_people:
            print(f"Failed to approve shares by {interaction.user.name}")
            await interaction.response.send_message("You are not authorized to approve shares.", ephemeral=True)
            return
        print(f"Approve button clicked by {interaction.user.name}")
        for item in self.children:
            item.disabled = True
        await interaction.response.edit_message(view=self)
        gs.start_approve_process(self.url)

        embed = build_embed(
            "✅ A submission has been approved!",
            f"""Submission for {self.url} has been approved by {interaction.user.name}.
This will shortly be shown in the Solar Website.""")
        await interaction.followup.send(embed=embed)

    @nc.ui.button(label="Deny", emoji="❌")
    async def cancel(self, button: nc.ui.Button, interaction: nc.Interaction):
        if interaction.user.id not in lists_of_approved_people:
            print(f"Failed to deny shares by {interaction.user.name}")
            await interaction.response.send_message("You are not authorized to deny shares.", ephemeral=True)
            return
        print(f"Cancel button clicked by {interaction.user.name}")
        for item in self.children:
            item.disabled = True
        await interaction.response.edit_message(view=self)

        embed = build_embed(
            "❌ A submission has been denied.",
            f"""Submission for {self.url} has been denied by {interaction.user.name}.
They can send a reason why it's been denied in the chat soon.""")
        await interaction.followup.send(embed=embed)

def send_share(url):
    if bot_loop is None:
        _pending.append(url)
        print("Bot not ready yet; queued command")
        return False
    asyncio.run_coroutine_threadsafe(post_share(url), bot_loop)
    return True

async def post_share(url):
    embed = build_embed(
        "A pending new share..",
        f"""———————————————————————————————————
{url}
———————————————————————————————————
Please review it, and approve or deny it by clicking the reaction below.
If you are not a developer, please avoid those buttons.""")

    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print(f"Couldn't find channel {CHANNEL_ID}")
        return

    view = Shares_Buttons(channel, url)
    await channel.send(embed=embed, view=view)
    print(f"Sent to channel {CHANNEL_ID}: {url}")

def start_bot():
    global client, bot_loop

    with open("token.txt", "r") as f:
        token = f.read().strip()

    activity = nc.Activity(
        type=nc.ActivityType.watching,
        name="pending shares..."
    )

    client = nc.Client(activity=activity)

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
