from errbot import BotPlugin, botcmd

class Ansible(BotPlugin):
    """Ansible plugin for Errbot."""

    @botcmd
    def ansible(self, msg, args):
        """Ansible executor"""
        return 'test' 
        #subprocess.check_output(['ls','-l'])
