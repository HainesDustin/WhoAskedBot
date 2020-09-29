# Sys imports
import logging
import os
import random

# Ext imports
import discord
from dotenv import load_dotenv
from foaas import fuck

# Configure our logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


class RudeResponder(discord.Client):

    async def on_ready(self):
        logging.info('Bot Ready')

    async def on_message(self, message):
        name = message.author.display_name
        logging.info('Message received from ' + name + ' in ' + message.channel.name)
        # Don't do anything if we sent the message
        if message.author == self.user:
            logging.info('Message was sent by the bot, discarding')
            return
        # Every message is a bit excessive, use some pseudo-randomness to change
        if random.randint(1, 10) % 3 != 0:
            logging.info('Bot won\'t send a reply this time')
            return
        msg = fuck.random(name=name, from_=' ').text[:-4]
        # Log our response
        logging.info('Preparing to send "' + msg + '" to ' + name)
        await message.channel.send(msg)


def main():
    # Initialise our token as an environment variable
    logging.info('Loading .env')
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        logging.error('DISCORD_TOKEN not defined in .env or missing, please check')
        exit(1)

    logging.info('Initialising client')
    client = RudeResponder()
    client.run(token)


if __name__ == '__main__':
    main()
