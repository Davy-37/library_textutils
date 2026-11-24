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
