# WhoAskedBot - "That friend"
### A simple bot that uses the FOAAS service to occasionally abuse those in your Discord

#### **Trigger Warning: Explicit Language**
This is just a quick project I threw together to try out some API stuff, as well as making a Discord bot. Most of the code is derived from guidance on [realpython.com](https://realpython.com/how-to-make-a-discord-bot-python)

## Usage
### Installation
1. Clone the repo and run `init.sh` to create a basic Python virtual environment and install dependencies
2. Create a new Discord application and configuring it with at least "Send Messages" and "Read Message History" permissions
3. Store your client token in `.env`
### Basic Usage
Run the bot with the following
```shell
python bot.py
```
## References
Thanks to the wonder of external libraries, I barely need to do anything to get this going. Docs on the external libraries used can be found here

[foaas-python](https://github.com/dmpayton/foaas-python)

[python-dotenv](https://github.com/theskumar/python-dotenv)

[discord.py](https://github.com/Rapptz/discord.py)

## Licensing
This is distributed under a MIT licence 