from errbot import BotPlugin, botcmd


class Ping(BotPlugin):

    @botcmd
    def ping(self, msg, args):
        """PONG!"""
        return 'PONG!'
