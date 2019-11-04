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

    #
    #
    #
    #
    async def on_ready(self):
        await self._handleDoorbell()

    #
    #
    #
    #
    async def _handleDoorbell(self):

        # getting channel
        id = int(os.getenv('CHANNEL'))
        channel = self.get_channel(id)

        # get mentions for members
        mentions = self._get_mentions(channel)

        # create content and send message, add image if MESSAGE_IMAGE is set
        content = os.getenv('MESSAGE_TEXT') + mentions
        if (os.getenv('MESSAGE_IMAGE')):
            content += os.getenv('MESSAGE_IMAGE')

        await channel.send(content=content)

    #
    #
    #
    #
    def _get_mentions(self, channel):

        mentions = ' @everyone '

        if (os.getenv('ROLE')):

            mentions = ''

            for member in channel.members:
                for role in member.roles:
                    if role.name == os.getenv('ROLE'):
                        mentions += ' ' + member.mention + ' '

        return mentions


# let it rain
mrdoorbell = MrDoorbell()
mrdoorbell.run(os.getenv('TOKEN'))
