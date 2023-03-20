import pytest
from utils.funcs import sort_data, pick_latest

@pytest.fixture()
def coll_original():
    return [{
        'state': 'EXECUTED',
        'date': '2019-08-26T10:50:58.294041'
    }, {
        'state': 'EXECUTED',
        'date': '2019-07-03T18:35:29.512364'
    }, {
        'state': 'EXECUTED',
        'date': '2018-06-30T02:08:58.425572'
    }, {
        'state': 'CANCELLED',
        'date': '2018-07-03T18:35:29.512364'
    }, {
        'state': 'EXECUTED',
        'date': '2019-05-30T02:04:58.425572'
    }, {
        'state': 'EXECUTED',
        'date': '2018-10-05T18:35:29.512364'
    }, {
        'state': 'EXECUTED',
        'date': '2019-10-05T18:35:29.512365'
    }]

@pytest.fixture()
def coll_sorted():
    return [{
        'state': 'EXECUTED',
        'date': '2019-10-05T18:35:29.512365'
    }, {
        'state': 'EXECUTED',
        'date': '2019-08-26T10:50:58.294041'
    }, {
        'state': 'EXECUTED',
        'date': '2019-07-03T18:35:29.512364'
    }, {
        'state': 'EXECUTED',
        'date': '2019-05-30T02:04:58.425572'
    }, {
        'state': 'EXECUTED',
        'date': '2018-10-05T18:35:29.512364'
    }, {
        'state': 'EXECUTED',
        'date': '2018-06-30T02:08:58.425572'
    }]

@ pytest.fixture()
def coll_of_5():
    return [{
        'state': 'EXECUTED',
        'date': '2019-10-05T18:35:29.512365'
    }, {
        'state': 'EXECUTED',
        'date': '2019-08-26T10:50:58.294041'
    }, {
        'state': 'EXECUTED',
        'date': '2019-07-03T18:35:29.512364'
    }, {
        'state': 'EXECUTED',
        'date': '2019-05-30T02:04:58.425572'
    }, {
        'state': 'EXECUTED',
        'date': '2018-10-05T18:35:29.512364'
    }]
def test_sort_data(coll_original, coll_sorted):
    assert sort_data(coll_original) == coll_sorted

def test_pick_latest(coll_sorted, coll_of_5):
    assert pick_latest(coll_sorted) == coll_of_5
