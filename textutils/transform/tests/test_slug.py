import pytest

from textutils import slugify


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Annual Report 2025", "annual-report-2025"),
        ("Café crème, déjà vu!", "cafe-creme-deja-vu"),
        ("Already-a-slug", "already-a-slug"),
        ("single", "single"),
        ("Ça coûte 5 € (TTC)", "ca-coute-5-ttc"),
    ],
)
def test_slugify(text, expected):
    assert slugify(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("", ""),
        ("   ", ""),
        ("!!! ???", ""),
        ("  leading and trailing  ", "leading-and-trailing"),
        ("many     spaces", "many-spaces"),
        ("a--b__c", "a-b-c"),
        ("日本語", ""),
    ],
)
def test_slugify_edge_cases(text, expected):
    assert slugify(text) == expected


@pytest.mark.parametrize(
    "separator, expected",
    [("_", "annual_report"), (".", "annual.report"), ("", "annualreport")],
)
def test_slugify_custom_separator(separator, expected):
    assert slugify("Annual Report", separator=separator) == expected


def test_slugify_rejects_a_non_string_separator():
    with pytest.raises(TypeError, match="separator must be a string"):
        slugify("Annual Report", separator=None)
