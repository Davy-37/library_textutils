"""Case conversion helpers."""

import re

_CAMEL_BOUNDARY = re.compile(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")
_WORD = re.compile(r"[^\W_]+")


def _split_camel_case(text):
    """
    Insert a space at each camelCase boundary of a text.

    Args:
        text (str): The text to split, e.g. "HTTPServerError".

    Returns:
        str: The text with spaces at the boundaries, e.g. "HTTP Server Error".
    """
    return _CAMEL_BOUNDARY.sub(" ", text)
