"""Input validation helpers shared by the public functions."""


def ensure_text(text):
    """Check that ``text`` is a string.

    Parameters
    ----------
    text : object
        The value to check.

    Raises
    ------
    TypeError
        If ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be a string, not {type(text).__name__}")
