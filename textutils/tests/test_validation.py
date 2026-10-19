import pytest

import textutils


@pytest.mark.parametrize(
    "function",
    [
        textutils.word_count,
        textutils.character_count,
        textutils.reverse,
        textutils.capitalize_words,
        textutils.snake_case,
        textutils.text_statistics,
    ],
)
@pytest.mark.parametrize("value", [None, 42, 3.14, ["a", "b"], b"bytes"])
def test_public_functions_reject_non_string_input(function, value):
    with pytest.raises(TypeError, match="text must be a string"):
        function(value)


def test_error_message_names_the_received_type():
    with pytest.raises(TypeError, match="not NoneType"):
        textutils.word_count(None)


def test_public_api_is_exposed_through_the_package():
    assert set(textutils.__all__) == {
        "capitalize_words",
        "character_count",
        "reverse",
        "snake_case",
        "text_statistics",
        "word_count",
    }
    for name in textutils.__all__:
        assert callable(getattr(textutils, name))
