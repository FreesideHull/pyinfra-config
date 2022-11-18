from pyinfra.api import FactBase
from pyinfra.operations import server
from pyinfra import host
class raw(FactBase):
    '''
    run raw command
    '''

    def command(self, command):
        return command

    def process(self, output):
        return '\n'.join(output)

update_out = host.get_fact(raw, command="dnf upgrade --refresh -y")
print(update_out)


server.reboot(delay=15, interval=1, reboot_timeout=300) # will reboot the target(s) and try to reconnect to them
