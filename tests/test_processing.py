import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(dictionary):
    """Тест на фильтрацию списка по значению ключа state, принятом по умолчанию (EXECUTED)."""
    assert filter_by_state(dictionary, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]