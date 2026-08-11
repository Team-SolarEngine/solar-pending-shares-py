# Solar Pending Shares
this just sends a embed for the [shared section in the solar website](https://solarengine.net/shares).

## Setting up
- Install Python latest.
- Have a 24/7 server running at all times.
- A Discord bot account. DON'T FUCKING USE YOUR ACCOUNT.
- Have git (obvious...)

```bash
# clone the repo repo repo
git clone https://github.com/Team-SolarEngine/solar-pending-shares
cd solar-pending-shares

# create token.txt beforehand dummy
echo "INPUT_DISCORD_TOKEN_FOR_YOUR_CLANKER" > token.txt
# don't leave this as `INPUT_DISCORD_TOKEN_FOR_YOUR_CLANKER` - replace it with your actual token
# also don't share or commit this file YOU WILL BE PWNED DUMMY!!

# do all python shit ig
python -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/python src/main.py
```
