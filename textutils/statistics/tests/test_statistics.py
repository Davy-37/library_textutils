import pytest

from textutils import text_statistics

TEXT = "The cat and the dog. The end!"


def test_text_statistics_counts():
    stats = text_statistics(TEXT)

    assert stats["characters"] == 29
    assert stats["characters_no_spaces"] == 23
    assert stats["words"] == 7
    assert stats["unique_words"] == 5
    assert stats["sentences"] == 2


def test_text_statistics_word_lengths():
    stats = text_statistics(TEXT)

    assert stats["average_word_length"] == pytest.approx(3.0)
    assert stats["shortest_word"] == "and"
    assert stats["longest_word"] == "and"


def test_text_statistics_most_frequent_word():
    stats = text_statistics(TEXT)

    assert stats["most_frequent_word"] == "the"
    assert stats["most_frequent_count"] == 3


def test_text_statistics_ties_are_broken_alphabetically():
    stats = text_statistics("zebra apple mango")

    assert stats["shortest_word"] == "apple"
    assert stats["longest_word"] == "apple"
    assert stats["most_frequent_word"] == "apple"


def test_text_statistics_ignores_case_and_punctuation():
    stats = text_statistics("Python, python! PYTHON?")

    assert stats["words"] == 3
    assert stats["unique_words"] == 1
    assert stats["most_frequent_word"] == "python"


def test_text_statistics_longest_and_shortest_words():
    stats = text_statistics("a quick extraordinary fox")

    assert stats["shortest_word"] == "a"
    assert stats["longest_word"] == "extraordinary"


@pytest.mark.parametrize("text", ["", "   ", "!!! ???"])
def test_text_statistics_without_words(text):
    stats = text_statistics(text)

    assert stats["words"] == 0
    assert stats["unique_words"] == 0
    assert stats["average_word_length"] == 0.0
    assert stats["shortest_word"] is None
    assert stats["longest_word"] is None
    assert stats["most_frequent_word"] is None
    assert stats["most_frequent_count"] == 0


def test_text_statistics_empty_text_counts():
    stats = text_statistics("")

    assert stats["characters"] == 0
    assert stats["characters_no_spaces"] == 0
    assert stats["sentences"] == 0


@pytest.mark.parametrize(
    "text, expected",
    [
        ("One sentence", 1),
        ("One. Two! Three?", 3),
        ("Wait... what?!", 2),
        ("No end mark", 1),
        ("...", 0),
    ],
)
def test_text_statistics_sentences(text, expected):
    assert text_statistics(text)["sentences"] == expected
