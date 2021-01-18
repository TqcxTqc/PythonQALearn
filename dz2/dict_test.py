import pytest


class TestDictMethods:

    def test_dict_copy(self, dict_key_string):
        """Check copy of the dictionary"""
        temp_dict = dict_key_string.copy()
        assert dict_key_string == temp_dict

    def test_dict_clear(self, dict_key_string):
        """Check dictionary after clearing"""
        dict_key_string.clear()
        assert dict_key_string == {}

    def test_dict_pop(self, dict_key_string):
        """Check correctness of removing an item from dictionary"""
        removed_item = dict_key_string.pop('two')
        assert dict_key_string == {'one': 1, 'three': 3}

    def test_dict_sorted_values(self, dict_key_string):
        """Check correctness sorted dictionary values"""
        assert sorted(dict_key_string.values()) == [1, 2, 3]

    @pytest.mark.parametrize("key, value", [('one', 1), ('two', 2), ('three', 3)])
    def test_dict_get_keys(self, dict_key_string, key, value):
        """Returns the value of the specified key"""
        assert dict_key_string.get(key) == value