import pytest

from textutils import snake_case


@pytest.mark.parametrize(
    "text, expected",
    [
        ("User Profile Settings", "user_profile_settings"),
        ("Quick brown fox!", "quick_brown_fox"),
        ("userName", "user_name"),
        ("HTTPServer", "http_server"),
        ("parseHTTPResponse", "parse_http_response"),
        ("Version2Beta", "version2_beta"),
        ("already_snake_case", "already_snake_case"),
        ("kebab-case-text", "kebab_case_text"),
        ("single", "single"),
    ],
)
def test_snake_case(text, expected):
    assert snake_case(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Total    Amount", "total_amount"),
        ("  leading and trailing  ", "leading_and_trailing"),
        ("__x__", "x"),
        ("a--b__c  d", "a_b_c_d"),
        ("", ""),
        ("   ", ""),
        ("!!!", ""),
    ],
)
def test_snake_case_edge_cases(text, expected):
    assert snake_case(text) == expected


def test_snake_case_regression_multiple_spaces():
    """Multiple consecutive spaces must produce a single underscore."""
    assert snake_case("Total   Amount") == "total_amount"
