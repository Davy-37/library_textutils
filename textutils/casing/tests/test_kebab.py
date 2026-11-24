import pytest

from textutils import kebab_case


@pytest.mark.parametrize(
    "text, expected",
    [
        ("User Profile Settings", "user-profile-settings"),
        ("parseHTTPResponse", "parse-http-response"),
        ("snake_case_text", "snake-case-text"),
        ("Version2Beta", "version2-beta"),
        ("already-kebab", "already-kebab"),
        ("single", "single"),
    ],
)
def test_kebab_case(text, expected):
    assert kebab_case(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("", ""),
        ("   ", ""),
        ("!!!", ""),
        ("  leading and trailing  ", "leading-and-trailing"),
        ("many     spaces", "many-spaces"),
        ("a--b__c", "a-b-c"),
    ],
)
def test_kebab_case_edge_cases(text, expected):
    assert kebab_case(text) == expected
