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


@pytest.mark.parametrize(
    "text, expected",
    [
        ("", ""),
        ("   ", ""),
        ("!!!", ""),
        ("  leading and trailing  ", "leadingAndTrailing"),
        ("many     spaces", "manySpaces"),
        ("a--b__c", "aBC"),
    ],
)
def test_camel_case_edge_cases(text, expected):
    assert camel_case(text) == expected
