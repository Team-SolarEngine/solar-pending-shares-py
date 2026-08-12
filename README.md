# Solar Pending Shares
This just sends a embed for the [shared section in the solar website](https://solarengine.net/shares). Here's a preview.

![Preview](./.github/readme/preview.png)

## Setting up
- Install Python latest.
- Have a 24/7 server running at all times.
- A Discord bot account. DON'T FUCKING USE A NON-BOT ACCOUNT.
- Have git (obvious...)

```bash
# clone the repo repo repo
git clone https://github.com/Team-SolarEngine/solar-pending-shares
cd solar-pending-shares

# do all python shit ig
python -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/python src/main.py
```

> [!IMPORTANT]
> Set up [@config.json.example](./config.json.example) beforehand. Rename it to `config.json` and fill in the values. Don't rename the file, duplicate it, and rename it to `config.json`.

> [!WARNING]
> Most importantly, DON'T FUCKING SHARE YOUR `config.json` FILE. You will be PWNED.

## Usage
Run `venv/bin/python src/main.py` to start the REST API and Bot (obvious lmao). To send requests, use the `POST /send_shares` endpoint with the appropriate JSON payload.

### Examples
**Bash** *(only used for testing.)*
```bash
curl -X POST http://127.0.0.1:8000/send_shares -H 'Content-Type: application/json' -d '{"url":"https://github.com/Team-SolarEngine/test-repo"}'
```

**JavaScript** *(only used for production.)*
```javascript
function sendShares(url) {
  fetch('http://127.0.0.1:8000/send_shares', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ "url": url }),
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
}
```
> [!NOTE]
> For TypeScript, just add `: string` to the `url` parameter. That's it!

> [!TIP]
> If you are actually using this for production, replace `http://127.0.0.1:8000` with your actual server URL.