from pyinfra.api import FactBase
from pyinfra import host
class raw(FactBase):
    '''
    run raw command
    '''

    def command(self, command):
        return command

    def process(self, output):
        return '\n'.join(output)

dfh_out = host.get_fact(raw, command='docker update --restart always $(docker ps -q)')
print(dfh_out)
