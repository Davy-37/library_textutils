"""URL slug generation."""

import re
import unicodedata

from textutils._validation import ensure_text

_NOT_ALPHANUMERIC = re.compile(r"[^a-z0-9]+")


def _to_ascii(text: str) -> str:
    """Replace accented letters by their unaccented ASCII equivalent.

    Characters without an ASCII equivalent are dropped.

    Parameters
    ----------
    text : str
        Text to convert, for example ``"café"``.

    Returns
    -------
    str
        The ASCII version of the text, for example ``"cafe"``.
    """
    decomposed = unicodedata.normalize("NFKD", text)
    return decomposed.encode("ascii", "ignore").decode("ascii")


def slugify(text: str, separator: str = "-") -> str:
    """Convert a string to a URL-friendly slug.

    Accented letters are replaced by their ASCII equivalent, the text is
    lowercased and every group of characters that is not a letter or a digit
    becomes a single separator. Leading and trailing separators are removed.

    Parameters
    ----------
    text : str
        Input text to convert.
    separator : str, default="-"
        String placed between the words of the slug.

    Returns
    -------
    str
        The slug. A text without any letter or digit returns an empty string.

    Raises
    ------
    TypeError
        If `text` or `separator` is not a string.

    Examples
    --------
    >>> slugify("Café crème, déjà vu!")
    'cafe-creme-deja-vu'
    >>> slugify("Annual  Report 2025", separator="_")
    'annual_report_2025'
    """
    ensure_text(text)
    if not isinstance(separator, str):
        raise TypeError(f"separator must be a string, not {type(separator).__name__}")
    words = _NOT_ALPHANUMERIC.sub(" ", _to_ascii(text).lower()).split()
    return separator.join(words)
