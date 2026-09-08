import pytest

from validkit import is_valid_email


@pytest.mark.parametrize(
    "text",
    [
        "user@example.com",
        "a@b.co",
        "user.name+tag@sub.example.org",
        "a@b.c2",
        "a@b.12",
    ],
)
def test_valid_emails(text: str) -> None:
    assert is_valid_email(text) is True


@pytest.mark.parametrize(
    "text",
    [
        "user@example",
        "user@example.c",
        "user example.com",
        "@example.com",
        "user@",
        "@",
        "user@@example.com",
        "user@example.com ",
        "user @example.com",
        "user\t@example.com",
        "user@example.co!",
    ],
)
def test_invalid_emails(text: str) -> None:
    assert is_valid_email(text) is False


@pytest.mark.parametrize("text", [42, None, 3.14, ["user@example.com"], b"user@example.com"])
def test_non_string_raises_type_error(text: object) -> None:
    with pytest.raises(TypeError):
        is_valid_email(text)  # type: ignore[arg-type]


@pytest.mark.parametrize("text", [42, 3.14, ["user@example.com"], {"a": "b"}])
def test_type_error_message_names_only_param_and_type(text: object) -> None:
    with pytest.raises(TypeError) as excinfo:
        is_valid_email(text)  # type: ignore[arg-type]

    message = str(excinfo.value)
    assert "text" in message
    assert "str" in message
    assert str(text) not in message
