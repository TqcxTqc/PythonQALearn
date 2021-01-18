import pytest


class TestListMethods:

    def test_list_append(self, string_list):
        """Check Added an element to the list"""
        string_list.append('mango')
        assert string_list == ['apple', 'banana', 'kiwi', 'mango']

    def test_reverse_list(self, string_list):
        """Check clearing elements from the list"""
        string_list.reverse()
        assert string_list == ['kiwi', 'banana', 'apple']

    def test_list_index(self, string_list):
        """Check index of element 'banana' in the list"""
        assert string_list.index('banana') == 1

    def test_remove_item(self, string_list):
        """Check removed item in the list"""
        string_list.remove('apple')
        assert string_list == ['banana', 'kiwi']

    @pytest.mark.parametrize("index, value", [(0, 'mango'), (1, 'potato'), (2, 'guawa')])
    def test_list_insert(self, string_list, index, value):
        """Check inserted items by index using params"""
        string_list.insert(index, value)
        modified_list = string_list[:]
        assert string_list == modified_list
