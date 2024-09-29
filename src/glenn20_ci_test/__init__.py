import rich

from ._version import version


def hello() -> None:
    rich.print(
        "[yellow][em]Hello[/em][/yellow] from [magenta]glenn20-ci-test![/magenta] "
        f"(version [cyan]{version}[/cyan])"
    )
