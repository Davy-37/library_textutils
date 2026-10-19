import pytest

from textutils import reverse


@pytest.mark.parametrize(
    "text, expected",
    [
        ("abc", "cba"),
        ("", ""),
        ("a", "a"),
        ("stressed", "desserts"),
        ("red blue", "eulb der"),
        (" padded ", " deddap "),
    ],
)
def test_reverse(text, expected):
    assert reverse(text) == expected


@pytest.mark.parametrize("text", ["", "a", "level", "red blue"])
def test_reverse_twice_returns_the_original_text(text):
    assert reverse(reverse(text)) == text
