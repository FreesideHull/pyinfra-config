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

dfh_out = host.get_fact(raw, command="df -h |grep -i 'dev/mapper'")
print(dfh_out)
