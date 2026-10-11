import pytest

from textutils import character_count, word_count


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Python", 1),
        ("The quick brown fox", 4),
        ("", 0),
        ("   ", 0),
        ("  leading and trailing  ", 3),
        ("many     spaces   between", 3),
        ("tabs\tand\nnewlines", 3),
        ("punctuation, counts! as part.", 4),
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("", 0),
        ("a", 1),
        ("quick fox", 9),
        ("  spaces  ", 10),
        ("line\nbreak", 10),
        ("café", 4),
    ],
)
def test_character_count(text, expected):
    assert character_count(text) == expected
