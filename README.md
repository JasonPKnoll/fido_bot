# Emoji Spreading Discord Bot

> A Discord bot who's main functionality is to spread emoji's throughout the server by adding them to existing members names. The bot has some additional functionality for moderation, which will be expanded upon in the future.

### Dependencies

* `Python 3.9.7`
* `python3 -m pip install -U discord.py`
* `dotenv`

### How to Use

* setup a new bot at [discord/developers](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications)
* create `.env` file
* Add your bots token in the `.env` file as `DISCORD_TOKEN=XXXXXXXX`
* run `python3 main.py`

### Admin Commands

> Admin commands will only trigger when an admin is the one giving it. Otherwise the bot will intentionally ignore it with no indication that the command exists. The settings for the server are hosted inside of a MongoDB database program. This allows the bot to be used in multiple servers, each one being able to set their own prefered emojis to spread throughout peoples names, and to have there own designated channel for the bot to forward users DM's to.


| Command          | Default Value | Example Input                | Description                                                                                                                                                                                                                                     |
|------------------|---------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| !setbotchannel   | Null          | !setbotchannel admin-channel | Sets the specified channel, which can be any that exists in the server. That channel will be given direct messages that users send to the bot. By default this channel is nothing, and no direct messages will be forwarded unless this is set. |
| !removeall       |               |                              | Removes all instances the set emoji from all users name in the server.                                                                                                                                                                          |
| !setemoji        | 🌽             | !setemoji 💕                  | Sets the emoji that will be added to users names based on the other bot commands.                                                                                                                                                               |
| !setaddword      | this          | !setaddword add              | The add word will add one emoji to any user that uses the word in a message.                                                                                                                                                                    |
| !setsubtractword | that          | !setsubtractword remove      | The remove word will remove every instance of the emoji from the user if they use it in a message.                                                                                                                                              |
| !setlotteryword  | spread        | !setlotteryword random       | The lottery word will be triggered if any user uses it in a message. When triggered the bot will add one emoji to five random users in the server with the exception of Admins.                                                                 |
| !values          |               |                              | This command will display the current emoji, adder word, subtractor word, and lottery word being used in the server.                                                                                                                            |
| !resetall        |               |                              | This command will reset the emoji, adder word, subtractor word, and lottery word back to its default values.                                                                                                                                    |



#### User Commands

>These are commands that any user can use to manually gain and give emojis to other users. The bot is unable to give emojis anyone who has more or equal authority to it within the server. Therefore it is unable to give emojis to Admins, and has also been set to ignore giving emojis to other bots.

| Command     | Example Input           | Description                                                                                                                                        |
|-------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| !giveme     | !giveme 10              | Adds the designated number of emojis to the users name up to the maximum that can be added based on the max characters left in the users nickname. |
| !transferto | !transferto @other_user 5 | Transfers the designated amount of emojis from one users name to the specified user name.                                                          |


#### Listeners for Memes
>Whats with all the corn in the Server? The corn, much like everything else in this section is an inside joke for the server that this bot was originally designed for.

| Listeners    | Description                                                                                                                                                                                                |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| corn         | When the bot detects any instance of the word "corn" it will respond with corn emojis, a corn quote, or yell about corn being spoken in its server. This includes gifs or urls that have corn in the name, and words that involve corn like corner or cornea. It is very sensitive to the word corn. Its a feature not a bug! |
| who          | When the bot detects any instance of the word "who" it will reply to the the comment with "who", wait 3 seconds and then reply with "cares".                                                               |
| I love fido  | When the bot detects "I love Fido" it will Direct Message the user who said it stating that they also love them, and then change their name in the server to "Fido's chew toy".                            |
| free me fido | When the bot detects "free me Fido" it will remove that users nickname reverting them back to there original name.                                                                                         |
