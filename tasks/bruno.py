from pyinfra.operations import server

server.shell(
    name="install Bruno",
    commands="flatpak install --noninteractive flathub com.usebruno.Bruno",
    _sudo=False,
)
