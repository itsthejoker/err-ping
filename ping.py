from errbot import BotPlugin, botcmd


class Ping(BotPlugin):
    """
    Am I alive?
    It's too early in the morning for such thoughts.

    ...in the meantime, though...

    >>> user: ping
    >>> errbot: PONG!
    """

    @botcmd
    def ping(self, msg, args):
        """
        PING!

        :param msg: Message object
        :param args: all words after the initial command
        :return: "PONG!"
        """
        return 'PONG!'
