"""Demonstration of common Python data types.

Run this script to see examples of the built-in data types
and a simple user-defined class.
"""


def show_none():
    """Example of the NoneType."""
    value = None
    print("NoneType example:", value, type(value))


def show_numerics():
    """Examples of numeric types: int, float and complex."""
    integer_val = 10
    float_val = 3.14
    complex_val = 2 + 3j
    print("Integer:", integer_val, type(integer_val))
    print("Float:", float_val, type(float_val))
    print("Complex:", complex_val, type(complex_val))


def show_bool():
    """Example of boolean values."""
    flag = True
    print("Boolean:", flag, type(flag))


def show_string_and_bytes():
    """Examples of text types: str and bytes."""
    text = "hello"
    raw = b"hello"
    print("String:", text, type(text))
    print("Bytes:", raw, type(raw))


def show_sequences():
    """Examples of sequence types: list, tuple and range."""
    sample_list = [1, 2, 3]
    sample_tuple = (1, 2, 3)
    sample_range = range(3)
    print("List:", sample_list, type(sample_list))
    print("Tuple:", sample_tuple, type(sample_tuple))
    print("Range:", list(sample_range), type(sample_range))


def show_sets():
    """Examples of set types: set and frozenset."""
    sample_set = {1, 2, 3}
    sample_frozenset = frozenset(sample_set)
    print("Set:", sample_set, type(sample_set))
    print("Frozenset:", sample_frozenset, type(sample_frozenset))


def show_mapping():
    """Example of mapping type: dict."""
    sample_dict = {"a": 1, "b": 2}
    print("Dict:", sample_dict, type(sample_dict))


class CustomType:
    """A simple user-defined class."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        return f"Hello, {self.name}!"


def show_custom_type():
    custom = CustomType("World")
    print("User-defined class:", custom.greet(), type(custom))


def main():
    """Run all examples."""

    show_none()
    show_numerics()
    show_bool()
    show_string_and_bytes()
    show_sequences()
    show_sets()
    show_mapping()
    show_custom_type()


if __name__ == "__main__":
    main()
