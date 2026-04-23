from pyinfra.operations import dnf

dnf.packages(name="install random tools", packages=[
    "bat",
], _sudo=True)