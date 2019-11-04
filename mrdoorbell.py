#
# MrDoorbell
#
#
# Installing:
#
# apt-get install python3-rpi.gpio
#
# pip3 install discord.py
# pip3 install python-dotenv
#
#

import discord
import os
import time
import RPi.GPIO as GPIO

from datetime import datetime, timedelta

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#
#
#
#
class MrDoorbell(discord.Client):

    EVERYONE = '@everyone'

    #
    #
    #
    async def on_ready(self):

        has_run = None
        channel = int(os.getenv('GPIO_PIN'))

        GPIO.setwarnings(False)

        # Use physical pin numbering
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        while True:
            now = datetime.timestamp(datetime.now())

            if GPIO.input(channel) == GPIO.HIGH && (has_run == None or has_run + timedelta(seconds=6000) <= now):
                has_run = now
                await self._handlePressDoorbell()

    #
    # if doorbell is pressed create message and send to channel
    #
    #
    async def _handlePressDoorbell(self):

        # getting channel
        id = int(os.getenv('CHANNEL'))
        channel = self.get_channel(id)

        # get mentions for members
        mentions = self._get_mentions(channel)

        # create content and send message, add image if MESSAGE_IMAGE is set
        content = os.getenv('MESSAGE_TEXT') + ' ' + mentions
        if (os.getenv('MESSAGE_IMAGE')):
            content += ' ' + os.getenv('MESSAGE_IMAGE')

        await channel.send(content=content)

    #
    # getting mentions for message
    # if role isset, check if members of channel have role,
    # if not mention @everyone
    #
    # @return String
    #
    def _get_mentions(self, channel):

        mentions = self.EVERYONE

        if (os.getenv('ROLE')):

            mentions = ''

            for member in channel.members:
                for role in member.roles:

                    # adding role
                    if role.name == os.getenv('ROLE'):
                        mentions += member.mention + ' '

            mentions = mentions.strip()

        return mentions


# let it rain
mrdoorbell = MrDoorbell()
mrdoorbell.run(os.getenv('TOKEN'))
