from pyinfra.operations import files, server
from pyinfra.operations import dnf, git

dnf.packages(name="install nvim and related packages", packages=[
    "nvim",
], _sudo=True)

files.sync(
    name="Install lazyvim starter",
    src="templates/lazyvim-starter/",
    dest="/home/hxl/.config/nvim/starter",
)
