from pyinfra.operations import dnf
from pyinfra.operations import server

extensions = [
    "adamhartford.vscode-base64",
    "adpyke.vscode-sql-formatter",
    "mechatroner.rainbow-csv",
    "medo64.render-crlf",
    "mrorz.language-gettext",
    "ms-python.python",
    "ms-python.vscode-pylance",
    "shardulm94.trailing-spaces",
    "wengerk.highlight-bad-chars",
    "golang.Go",
    "ms-python.black-formatter",
]


dnf.key(
    name="add Microsoft GPG key",
    src="https://packages.microsoft.com/keys/microsoft.asc",
    _sudo=True,
)


dnf.repo(
    name="add vscode repo",
    src="vscode",
    baseurl="https://packages.microsoft.com/yumrepos/vscode",
    gpgcheck=True,
    gpgkey="https://packages.microsoft.com/keys/microsoft.asc",
    enabled=True,
    _sudo=True,
)

dnf.packages(name="install VS Code", packages=["code"], _sudo=True)


for extension in extensions:
    server.shell(
        name=f"Ensure VS Code extension {extension} is installed",
        commands=f"code --list-extensions | grep -q {extension} || code --install-extension {extension}",
        _sudo=False,
    )

