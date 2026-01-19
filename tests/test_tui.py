import pytest


from epitech_console import TUI
from epitech_console.ANSI import Color
from epitech_console import (init, quit)


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


def test_tui_limit(
    ) -> None:
    t = TUI(2, 2, limit=(2, 2, 2, 2))
    assert t.selected == (1, 1)


def test_tui_string(
    ) -> None:
    t = TUI(1, 1)
    assert str(t).count("\n") == 2


def test_tui_add_smaller_than_spot(
    ) -> None:
    t = TUI(1, 1)
    t.add(1, 1, "test")
    assert "test" in t._screen[0][0]["name"]


def test_tui_add_bigger_than_spot(
    ) -> None:
    t = TUI(1, 1)
    t.add(1, 1, ("-" * 100))
    assert "-" in t._screen[0][0]["name"] and not ("-" * 100) in t._screen[0][0]["name"]


def test_tui_add_action(
    ) -> None:
    f = lambda x: x * 2
    t = TUI(1, 1)
    t.add(1, 1, "test", action=f)
    assert t._screen[0][0]["action"] == f


def test_tui_add_data(
    ) -> None:
    t = TUI(1, 1)
    t.add(1, 1, "test", data=84)
    assert t._screen[0][0]["data"] == 84


def test_tui_add_color(
    ) -> None:
    c=Color(Color.C_RESET)
    t = TUI(1, 1)
    t.add(1, 1, "test", color=c)
    assert t._screen[0][0]["color"] == c


def test_tui_delete(
    ) -> None:
    t = TUI(1, 1)
    t.add(1, 1, "test")
    assert "test" in t._screen[0][0]["name"]
    t.delete(1, 1)
    assert not "test" in t._screen[0][0]["name"] and " " in t._screen[0][0]["name"]


def test_tui_fill_smaller_than_spot(
    ) -> None:
    t = TUI(1, 1)
    t.fill("test")
    assert "test" in t._screen[0][0]["name"]


def test_tui_fill_bigger_than_spot(
    ) -> None:
    t = TUI(1, 1)
    t.fill("-" * 100)
    assert "-" in t._screen[0][0]["name"] and not ("-" * 100) in t._screen[0][0]["name"]


def test_tui_move(
    ) -> None:
    t = TUI(2, 2)
    t.move(2, 2)
    assert t.selected == (1, 1)


quit(delete_log=True)
