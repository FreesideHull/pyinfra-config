from pyinfra.operations import dnf, server

dnf.update()
server.reboot(delay=10, interval=1, reboot_timeout=300)
# any post reboot commands here
