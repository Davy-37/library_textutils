"""Text reversal helpers."""

from textutils._validation import ensure_text


def reverse(text: str) -> str:
    """Reverse the characters of a string.

    Parameters
    ----------
    text : str
        Input text to reverse.

    Returns
    -------
    str
        The input text with its characters in reverse order.

    Raises
    ------
    TypeError
        If `text` is not a string.

    Examples
    --------
    >>> reverse("stressed")
    'desserts'
    """
    ensure_text(text)
    return text[::-1]
