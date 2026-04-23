from pyinfra.operations import files
from pyinfra.operations import dnf, server

dnf.packages(name="install sway", packages=[
    "fuzzel",
    "sway",
], _sudo=True)


files.template(
    name="Install sway config",
    src="templates/sway",
    dest="/etc/sway/config",
    mode="644",
    user="root",
    group="root",
    _sudo=True,
)

files.template(
    name="Install fuzzel config",
    src="templates/fuzzel",
    dest="/home/hxl/.config/fuzzel/fuzzel.ini",
    mode="644",
)

files.template(
    name="Install hxstatus.py",
    src="templates/hxstatus.py",
    dest="/home/hxl/hxstatus.py",
    mode="644",
)
