import pytest


from epitech_console import TUI
from epitech_console import init, quit


init()


def test_tui_initialization(
    ) -> None:
    t = TUI(1, 1)
    assert len(t._screen) == 1 == len(t._screen[0])


def test_tui_invalid_initialization(
    ) -> None:
    t1 = TUI(0, 1)
    t2 = TUI(1, 0)
    t3 = TUI(0, 0)
    assert not hasattr(t1, "_screen")
    assert not hasattr(t2, "_screen")
    assert not hasattr(t3, "_screen")


quit(delete_log=True)
