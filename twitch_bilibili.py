import time

import irc.bot
import requests


class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        # Get the channel id, we will need this for v5 API calls
        url = 'https://api.twitch.tv/kraken/users?login=' + channel
        headers = {'Client-ID': client_id,
                   'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r['users'][0]['_id']

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print('Connecting to ' + server + ' on port ' + str(port) + '...')
        irc.bot.SingleServerIRCBot.__init__(self,
                                            [(server, port, 'oauth:' + token)],
                                            username, username)

    def on_welcome(self, c, e):
        print('Joining ' + self.channel)

        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        # If a chat message starts with an exclamation point, try to run it as a command
        cmd = e.arguments[0]
        uname = e.tags[3]["value"]
        print(cmd)
        return


def bot():
    bot = TwitchBot("", "",
                    "", "")
    bot.start()


# bot()

import urllib.request
import os
import json

if not os.path.exists('./emotes'):
    os.makedirs('./emotes')
print('Saving emotes to folder: ' + os.path.abspath('./emotes') + '...')
print('Grabbing emote list...')
emotes = json.load(urllib.request.urlopen('https://api.twitch.tv/kraken/chat/emoticons/'))
for emote in emotes['emoticons']:
    code = emote['regex']
    print('Downloading: ' + code + '...')
    urllib.request.urlretrieve(emote['images'][0]['url'], './emotes/' + code + '.png')
print('Done! Kappa')
