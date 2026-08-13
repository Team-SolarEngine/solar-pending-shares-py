import nextcord as nc
import time

def build_embed(title, description):
    embed = nc.Embed(
        description=f"""# {title}
{description}
> *Posted at <t:{int(time.time())}:S>*""",
        color=nc.Color(0xdd2ef4),
    )
    return embed

class Reject_Modal(nc.ui.Modal):
    def __init__(self, channel, url, view, message):
        super().__init__(title="Reject Submission")
        self.channel = channel
        self.url = url
        self.view = view
        self.message = message

        self.reason = nc.ui.TextInput(
            label="Reason of rejection",
            placeholder="The mod/script is full of viruses and leaks your personal data...",
            required=True,
            style=nc.TextInputStyle.paragraph
        )

        self.add_item(self.reason)

    async def callback(self, interaction: nc.Interaction):
        await interaction.response.defer()

        embed = build_embed(
            "❌ A submission has been denied.",
            f"""Submission for {self.url} has been denied by <@{interaction.user.id}>.
**Given reason**; {self.reason.value}""")
        await interaction.followup.send(embed=embed)

        print(f"Cancel button clicked by {interaction.user.name}.\n  Reason; {self.reason.value}")

        await self.message.edit(view=self.view)
