"""Statistics about a text."""

import re
import string
from collections import Counter

from textutils._validation import ensure_text

_SENTENCE_END = re.compile(r"[.!?]+")


def _normalize_words(text: str) -> list[str]:
    """Split a text into lowercase words without surrounding punctuation.

    Parameters
    ----------
    text : str
        Text to split.

    Returns
    -------
    list of str
        The normalized words, in order of appearance. Words made only of
        punctuation are dropped.
    """
    words = (word.strip(string.punctuation) for word in text.lower().split())
    return [word for word in words if word]


def _count_sentences(text: str) -> int:
    """Count the sentences of a text.

    Sentences end with ``.``, ``!`` or ``?``; consecutive marks count once and
    empty fragments are ignored.

    Parameters
    ----------
    text : str
        Text to analyze.

    Returns
    -------
    int
        Number of sentences.
    """
    return sum(1 for part in _SENTENCE_END.split(text) if part.strip())


def _average_length(words: list[str]) -> float:
    """Compute the average length of a list of words.

    Parameters
    ----------
    words : list of str
        Words to measure.

    Returns
    -------
    float
        Average word length, or ``0.0`` when there is no word.
    """
    if not words:
        return 0.0
    return sum(len(word) for word in words) / len(words)


def _most_frequent(words: list[str]) -> tuple[str | None, int]:
    """Find the most frequent word.

    Parameters
    ----------
    words : list of str
        Words to analyze.

    Returns
    -------
    tuple of (str or None, int)
        The most frequent word and its number of occurrences. Ties are broken
        alphabetically. ``(None, 0)`` is returned when there is no word.
    """
    if not words:
        return None, 0
    counts = Counter(words)
    word = min(counts, key=lambda candidate: (-counts[candidate], candidate))
    return word, counts[word]


def text_statistics(text: str) -> dict[str, int | float | str | None]:
    """Calculate statistics about ``text``.

    The statistics include character, word, sentence, word length,
    and word frequency information.

    Args:
        text: The text to analyze.

    Returns:
        A dictionary containing the statistics of the text.

    Example:
        >>> text_statistics("The cat and the dog. The end!")
        {
            'characters': 29,
            'characters_no_spaces': 23,
            'words': 7,
            'unique_words': 5,
            'sentences': 2,
            'average_word_length': 3.0,
            'shortest_word': 'and',
            'longest_word': 'and',
            'most_frequent_word': 'the',
            'most_frequent_count': 3
        }
    """
    ensure_text(text)
    words = _normalize_words(text)
    most_frequent_word, most_frequent_count = _most_frequent(words)

    return {
        "characters": len(text),
        "characters_no_spaces": sum(1 for char in text if char != " "),
        "words": len(words),
        "unique_words": len(set(words)),
        "sentences": _count_sentences(text),
        "average_word_length": _average_length(words),
        "shortest_word": min(words, key=lambda word: (len(word), word), default=None),
        "longest_word": min(words, key=lambda word: (-len(word), word), default=None),
        "most_frequent_word": most_frequent_word,
        "most_frequent_count": most_frequent_count,
    }
