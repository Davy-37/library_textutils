"""Word and character counters."""

from textutils._validation import ensure_text


def word_count(text: str) -> int:
    """Count the number of words in a string.

    Words are sequences of characters separated by whitespace.

    Parameters
    ----------
    text : str
        Input text whose words are counted.

    Returns
    -------
    int
        Number of words in the input text.

    Raises
    ------
    TypeError
        If `text` is not a string.

    Examples
    --------
    >>> word_count("The quick brown fox jumps")
    5
    >>> word_count("")
    0
    """
    ensure_text(text)
    return len(text.split())


def character_count(text: str) -> int:
    """Count the number of characters in a string, spaces included.

    Parameters
    ----------
    text : str
        Input text whose characters are counted.

    Returns
    -------
    int
        Number of characters in the input text.

    Raises
    ------
    TypeError
        If `text` is not a string.

    Examples
    --------
    >>> character_count("quick fox")
    9
    """
    ensure_text(text)
    return len(text)
