from pyinfra.operations import server

server.shell(
    name="purge all unused docker assets",
    commands=["docker system prune -fa"],
)
