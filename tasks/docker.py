from pyinfra import host
from pyinfra.facts.files import File
from pyinfra.facts.server import User
from pyinfra.operations import dnf, server

user = host.get_fact(User)

def docker_repo_missing():
    return not host.get_fact(File, path="/etc/yum.repos.d/docker-ce.repo")

dnf.packages(
    name="Install dnf-plugins-core",
    packages=["dnf-plugins-core"],
    _sudo=True,
)

server.shell(
    name="Add Docker repository using dnf config-manager",
    commands=[
        "dnf config-manager addrepo --from-repofile https://download.docker.com/linux/fedora/docker-ce.repo"
    ],
    _sudo=True,
    _if=docker_repo_missing,
)

dnf.packages(
    name="Install Docker packages",
    packages=[
        "docker-ce",
        "docker-ce-cli",
        "containerd.io",
        "docker-buildx-plugin",
        "docker-compose-plugin",
    ],
    _sudo=True,
)

server.user(
    name="Add current user to docker group",
    user=user,
    groups=["docker"],
    append=True,
    _sudo=True,
)