from errbot import BotPlugin, botcmd, subprocess

class Ansible(BotPlugin):
    """Example 'Hello, world!' plugin for Errbot"""

    @botcmd
    def ansible(self, msg, args):
        """Say hello to the world"""
        return subprocess.check_output(['ls','-l'])
