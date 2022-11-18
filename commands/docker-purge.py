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

vac_out = host.get_fact(raw, command="docker system prune -fa")
print(vac_out)
