import pytest

from glenn20_ci_test import hello


def test_hello(capsys: pytest.CaptureFixture[str]) -> None:
    hello()
    captured = capsys.readouterr()
    assert captured.out.startswith("Hello from glenn20-ci-test! (version")
