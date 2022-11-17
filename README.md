# pyinfra-config
pyinfra config for using administering Freeside machines

## System Requirements
    
- Python 3 + pip  
- [pipx](https://pypa.github.io/pipx/installation/)  
- Linux (Windows may work but is untested)  

## Getting Started

- `pipx install pyinfra`  
- be connected to the UoH VPN or be on their network  
- have a valid SSH config file. (A valid file can be seen below)  
	- must use publickey authentication  
	- must have added your key to each machine in host list beforehand with `ssh-copy-id`  


### Example SSH config

```
Host fs-web02
        Hostname freeside.co.uk
        User username
        PreferredAuthentications        publickey,password,keyboard-interactive
Host fs-storage
        Hostname 150.237.94.147
        User username
        PreferredAuthentications        publickey,password,keyboard-interactive
Host fs-docker
        Hostname 150.237.94.41
        User username
        PreferredAuthentications        publickey,password,keyboard-interactive
Host fs-docker2
        Hostname 150.237.94.53
        User username
        PreferredAuthentications        publickey,password,keyboard-interactive
Host fs-ipa
        Hostname 150.237.94.146
        User username
        PreferredAuthentications        publickey,password,keyboard-interactive


Host fs-desktop-01
        Hostname 150.237.94.40
        User username
        PreferredAuthentications        publickey,password,keyboard-interactive
Host fs-desktop-02
        Hostname 150.237.94.3
        User username
        PreferredAuthentications        publickey,password,keyboard-interactive
Host fs-desktop-03
        Hostname 150.237.94.30
        User userame
        PreferredAuthentications        publickey,password,keyboard-interactive
Host fs-desktop-04
        Hostname 150.237.94.39
        User userame
        PreferredAuthentications        publickey,password,keyboard-interactive
```

### To Run

To run your commands: `pyinfra hosts/choose-your-group.py commands/choose-your-script.py` (hosts.py is all fs machines)
or
`pyinfra target-name exec -- command` where command is a valid terminal command on the target e.g. `ls`
or
`pyinfra target-name pyinfra-command`
## Snippets

inside this repo you will find some pyinfra snippets that you may find useful. Such as patching a system or verifying a user exists and they own their home directory.  

## Changelog
- commit your changes
- generate the changelog with `./changelog` or `bash /path/to/changelog` (make sure it is executable with `chmod +x`)
- `git add . && git commit --amend --no-edit ` to amend your changes before pushing
- See the [Changelog](/CHANGELOG)
  


## License

pyinfra-config is released under the MIT. The full license text is included in the LICENSE file in this repository. Tldr legal have a [great summary](https://tldrlegal.com/license/mit-license) of the license if you're interested.
