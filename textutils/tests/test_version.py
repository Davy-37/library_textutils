from importlib.metadata import PackageNotFoundError, version

import pytest

import textutils


def test_version_is_a_semantic_version():
    if textutils.__version__ == "unknown":
        pytest.skip("the package is not installed")
    major, minor, patch = textutils.__version__.split(".")

    assert major.isdigit() and minor.isdigit() and patch.isdigit()


def test_version_matches_the_package_metadata():
    try:
        installed = version("textutils-davy")
    except PackageNotFoundError:
        pytest.skip("the package is not installed")

    assert textutils.__version__ == installed
