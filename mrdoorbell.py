#
#
#
# pip3 install discord.py
# pip3 install python-dotenv
#

import discord
import re as regex
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#
#
#
#
class MrDoorbell(discord.Client):

    async def on_ready(self):
        await self._handleDoorbell()

    async def _handleDoorbell(self):

        # getting channel
        id = int(os.getenv('CHANNEL'))
        current_channel = self.get_channel(id)

        # embed message
        embed = discord.Embed(title=os.getenv('MESSAGE_TITLE'), color=discord.Colour.red(), description=os.getenv('MESSAGE_TEXT'))
        embed.set_image(url=os.getenv('MESSAGE_IMAGE'))

        # send message
        await current_channel.send(embed=embed)

# let it rain
mrdoorbell = MrDoorbell()
mrdoorbell.run(os.getenv('TOKEN'))
