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
    """Calculate statistics about a string.

    Words are lowercased and stripped of surrounding punctuation. Ties for the
    shortest, longest and most frequent word are broken alphabetically.

    Parameters
    ----------
    text : str
        Input text to analyze.

    Returns
    -------
    dict
        Statistics of the text with the following keys:

        - ``characters`` (int): number of characters.
        - ``characters_no_spaces`` (int): number of characters, spaces excluded.
        - ``words`` (int): number of words.
        - ``unique_words`` (int): number of distinct words.
        - ``sentences`` (int): number of sentences.
        - ``average_word_length`` (float): average length of the words.
        - ``shortest_word`` (str or None): shortest word.
        - ``longest_word`` (str or None): longest word.
        - ``most_frequent_word`` (str or None): most frequent word.
        - ``most_frequent_count`` (int): occurrences of the most frequent word.

        Word fields are ``None`` and counts are ``0`` for an empty text.

    Raises
    ------
    TypeError
        If `text` is not a string.

    Examples
    --------
    >>> stats = text_statistics("The cat and the dog. The end!")
    >>> stats["words"], stats["sentences"]
    (7, 2)
    >>> stats["most_frequent_word"], stats["most_frequent_count"]
    ('the', 3)
    >>> text_statistics("")["shortest_word"] is None
    True
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
