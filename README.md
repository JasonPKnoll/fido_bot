# Simple discord bot
A simple discord bot that has an obsession with adding emoji's to peoples names

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

* #### Admin Features
* Typing `!setbotchannel` followed by channel name will make that channel the `"designated bot channel"` for admin commands and forwarding messages from bot DM's
* Typing `!removeall` in the `"designated bot channel"` will remove all of the designated emoji's from all members names
* Typing `!setemoji` in the `"designated bot channel"` allows the `"default emoji"` to be changed to any specified emoji following the command
  * Ex: `!setemoji 💕`
* Typing `!setaddword` in the `"designated bot channel"` followed by desired word allows the default `"adder word"` to be changed
* Typing `!setsubtractword` in the `"designated bot channel"` followed by desired word allows the default `"subtractor word"` to be changed
* Typing `!setplagueword` in the `"designated bot channel"` followed by desired word allows the default `"plaguing word"` to be changed
* Typing `!values` in the `"designated bot channel"` will display the current bot settings

* DM's sent to the bot are forwarded to the `"designated bot channel"`.

* #### Basic Features
* Anytime someone types the `adder word` defaulted to `"this"` in a sentence they and anyone they mentioned gets one emoji added to their name
* Anytime someone types the `subtractor word` defaulted to `"that"` in a sentence all of their emoji's are removed from their name
* Anytime someone types the `plague word` defaulted to `"spread"` in a sentence causes one emoji to be put on 5 random members names
* A member typing `!infectme` followed by a number will give that member the desired number of emoji's onto the end of their name or the max allowed if it goes over the character limit.
  * Ex: `!infectme 4`
* A member typing `!transferto` followed by mentioning another member and then a number will transfer the specified number of emoji's to the mentioned member.
  * Ex: `!transferto @examplemember 3`
