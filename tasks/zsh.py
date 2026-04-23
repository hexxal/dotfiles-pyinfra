from pyinfra.operations import files, server
from pyinfra.operations import dnf

dnf.packages(name="install zsh and related packages", packages=[
    "zsh",
    "fzf",
], _sudo=True)

server.user(
    name="Set default shell to zsh",
    user="hxl",
    shell="/bin/zsh",
    _sudo=True,
)

files.template(
    name="Install .zshrc",
    src="templates/zshrc",
    dest="/home/hxl/.zshrc",
)