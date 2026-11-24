import pytest

from textutils import capitalize_words


@pytest.mark.parametrize(
    "text, expected",
    [
        ("the quick brown fox", "The Quick Brown Fox"),
        ("mIXED cASE tExt", "Mixed Case Text"),
        ("single", "Single"),
        ("", ""),
        ("already Capitalized", "Already Capitalized"),
        ("two  spaces", "Two  Spaces"),
        ("  padded  ", "  Padded  "),
    ],
)
def test_capitalize_words(text, expected):
    assert capitalize_words(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("red\tblue", "Red\tBlue"),
        ("red\nblue\ngreen", "Red\nBlue\nGreen"),
    ],
)
def test_capitalize_words_regression_tabs_and_line_breaks(text, expected):
    """Every word is capitalized, whatever the whitespace separating them."""
    assert capitalize_words(text) == expected
