import pytest


class TestStringMethod:

    def test_string_isAlpha(self, string_wasd):
        """Check if all characters in the string are in the alphabet"""
        assert string_wasd.isalpha()

    def test_string_upper(self, string_wasd, string_WASD):
        """Check if string characters are capitalized"""
        assert string_wasd.upper() == string_WASD

    def test_string_lower(self, string_WASD, string_wasd):
        """Check capitalized string characters are in lower """
        assert string_WASD.lower() == string_wasd

    def test_string_endswith(self, string_wasd):
        """Check string characters ends as 'sd' """
        assert string_wasd.endswith('sd')

    @pytest.mark.parametrize("keys, index", [('w', 0), ('a', 1), ('s', 2), ('d', 3)])
    def test_string_index(self, string_wasd, keys, index):
        """Searches the string for a specified value and returns the position of where it was found"""
        assert string_wasd.index(keys) == index
