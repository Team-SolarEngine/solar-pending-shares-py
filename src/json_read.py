"""
Module for reading configuration from a JSON file.

Available Imports:
    BOT_TOKEN,
    CHANNEL_ID,
    LISTS_OF_APPROVED_PEOPLE
"""

import json

with open("config.json", "r") as f:
    config = json.load(f)

BOT_TOKEN = config["bot_token"]
CHANNEL_ID = int(config["channel_id"])
LISTS_OF_APPROVED_PEOPLE = [int(id) for id in config["lists_of_approved_people"]]