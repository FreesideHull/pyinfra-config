from pyinfra.operations import server, files

username = input("enter the username of the account you wish to verify: ")  #explains itself, fetches the user

server.user(
    name="Validate user", # or create them if they somehow don't exist
    user=username,
    home="/home/"+username,
    _sudo=True,
)

files.directory(
    name="Ensure /home/username exists", # create the folder, if its a new user it is unlikely to exist
    path="/home/"+username,
    user=username,
    group=username,
    _sudo=True,
)