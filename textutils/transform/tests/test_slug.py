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
