"""Text reversal helpers."""


def reverse(text: str) -> str:
    """Reverse ``text``.

    Args:
        text: The text to reverse.

    Returns:
        The text with its characters in reverse order.

    Example:
        >>> reverse("abc")
        'cba'
    """
    return text[::-1]
