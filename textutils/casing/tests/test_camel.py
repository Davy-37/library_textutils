import pytest

from textutils import camel_case


@pytest.mark.parametrize(
    "text, expected",
    [
        ("User Profile Settings", "userProfileSettings"),
        ("parse_http_response", "parseHttpResponse"),
        ("kebab-case-text", "kebabCaseText"),
        ("HTTPServer", "httpServer"),
        ("alreadyCamel", "alreadyCamel"),
        ("Version 2 Beta", "version2Beta"),
        ("single", "single"),
    ],
)
def test_camel_case(text, expected):
    assert camel_case(text) == expected
