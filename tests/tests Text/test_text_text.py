import pytest


from epitech_console.ANSI import ANSI
from epitech_console.Text import Text
from epitech_console import init, quit


init()


def test_text_string_initialization(
    ) -> None:
    t = Text("hello")
    assert str(t) == "hello"


def test_text_ANSI_initialization(
    ) -> None:
    t = Text(ANSI("hello"))
    assert str(t) == "hello"


def test_ansi_list_init(
    ) -> None:
    a = Text(["Hello", " World", "!!!"])
    assert str(a) == "Hello World!!!"


def test_text_empty_initialization(
    ) -> None:
    t = Text()
    assert str(t) == ""


def test_text_length(
    ) -> None:
    t = Text("hello")
    assert len(t) == 5


def test_text_repr(
    ) -> None:
    t = Text("hello")
    assert repr(t) == "Text(\'hello\')"


def test_text_url_link_no_text(
    ) -> None:
    link = Text.url_link("https://example.com")
    assert "\x1b]8;;https://example.com\x1b\\" in str(link)
    assert "\x1b]8;;\x1b\\" in str(link)


def test_text_url_link_custom_text(
    ) -> None:
    link = Text.url_link("https://example.com", text="CLICK")

    assert str(link) == '\x1b]8;;https://example.com\x1b\\CLICK\x1b]8;;\x1b\\'


def test_text_url_link_escape_sequences(
    ) -> None:
    link = Text.url_link("https://example.com/test")

    assert str(link) == '\x1b]8;;https://example.com/test\x1b\\https://example.com/test\x1b]8;;\x1b\\'


def test_text_file_link_simple(
    ) -> None:
    link = Text.file_link("/tmp/file.py")

    assert str(link) == '\x1b]8;;jetbrains://clion/navigate/reference?file=/tmp/file.py\x1b\\File "/tmp/file.py"\x1b]8;;\x1b\\'


def test_text_file_link_line_number(
    ) -> None:
    link = Text.file_link("/tmp/file.py", line=42)

    assert str(link) == '\x1b]8;;jetbrains://clion/navigate/reference?file=/tmp/file.py&line=42\x1b\\File "/tmp/file.py", line 42\x1b]8;;\x1b\\'


quit(delete_log=True)
