from errbot import BotPlugin, botcmd

class Ansible(BotPlugin):
    """Example 'Hello, world!' plugin for Errbot"""

    @botcmd
    def ansible(self, msg, args):
        """Say hello to the world"""
        return "Hello, world!"
