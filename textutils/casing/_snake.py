"""Snake case conversion."""

from textutils._validation import ensure_text
from textutils.casing._words import split_words


def snake_case(text: str) -> str:
    """Convert a string to snake case.

    Words may be separated by spaces, hyphens, underscores or camelCase
    boundaries. Punctuation is removed and repeated separators are collapsed.

    Parameters
    ----------
    text : str
        Input text to convert.

    Returns
    -------
    str
        The text in lowercase, with words joined by underscores. An empty or
        whitespace-only text returns an empty string.

    Raises
    ------
    TypeError
        If `text` is not a string.

    Examples
    --------
    >>> snake_case("User Profile Settings")
    'user_profile_settings'
    >>> snake_case("parseHTTPResponse")
    'parse_http_response'
    """
    ensure_text(text)
    return "_".join(word.lower() for word in split_words(text))
