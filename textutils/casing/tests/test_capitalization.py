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
