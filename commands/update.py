from pyinfra.operations import dnf, server

dnf.update() # assumes the target(s) use RHEL based distros. Here at Freeside we use Fedora. replace with whatever package manager you use on your targets. pyinfra can do its own scanning to find which package manager is in use to automate that for you - pretty cool huh 
server.reboot(delay=10, interval=1, reboot_timeout=300) # will reboot the target(s) and try to reconnect to them
# any post reboot commands here
