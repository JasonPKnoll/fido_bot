# Simple discord bot
A simple discord bot that has an obsession with 🌽

### Dependencies

* `Python 3.9.7`
* `python3 -m pip install -U discord.py`
* `dotenv`

### How to Use

* setup a new bot at [discord/developers](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications)
* create `.env` file
* Add your bots token in the `.env` file as `DISCORD_TOKEN=XXXXXXXX`
* run `python3 main.py`

### Features

* anytime someone types `this` in a sentence they and anyone they mentioned gets 🌽 added to their name
* anytime someone types `that` in a sentence all of their 🌽  is removed from their name
* typing `spread` in a sentence causes 🌽  to be put on 5 random members names
* typing `🌽 removeall` in a channel designated `fido-playground` will remove all 🌽 from all members names
