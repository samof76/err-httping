from errbot import BotPlugin, arg_botcmd, botcmd
import requests

class Httping(BotPlugin):

    @botcmd
    def hello_httping(self, msg, args):
        """Say hello to httping"""
        return 'Hi there! Welcome to httping'

    @arg_botcmd('url', type=str)
    def httping(self, msg, url=None):
        """Sends a HTTP GET request to the url and returns the status code"""
        r = requests.get(url)
        return r.status_code


