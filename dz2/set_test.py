import pytest


class TestSetMethods:
    def test_set_add(self, set_items):
        """Check added new item in to set"""
        set_items.add('train')
        assert set_items == {'car', 'bike', 'bus', 'train'}

    def test_set_discard(self, set_items):
        """Check that removed item is not in set"""
        set_items.discard('bike')
        assert set_items == {'car', 'bus'}

    def test_set_union(self, set_items, set_items_for_union):
        unified_set = set_items.union(set_items_for_union)
        assert unified_set == {'car', 'bike', 'bus', 1, 2, 3}

    def test_set_clear(self, set_items):
        set_items.clear()
        assert set_items == set()

    def test_set_remove(self, set_items, set_test_params):
        """Removes the specified element"""
        set_items.remove(set_test_params[0])
        assert set_items == set_test_params[1]
