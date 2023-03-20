import datetime

from utils.class_operate import Operation
import pytest

@pytest.fixture()
def coll():
    return {
        'id': 441945886,
        'state': 'EXECUTED',
        'date': '2019-08-26T10:50:58.294041',
        'operationAmount': {
            'amount': '31957.58',
            'currency': {
                'name': 'руб.',
                'code': 'RUB'}},
        'description': 'Перевод организации',
        'from': 'Visa Classic 1596837868705199',
        'to': 'Счет 64686473678894779589'
    }
@pytest.fixture()
def coll_1():
    return {
        'id': 441945886,
        'state': 'EXECUTED',
        'date': '2019-08-26T10:50:58.294041',
        'operationAmount': {
            'amount': '31957.58',
            'currency': {
                'name': 'руб.',
                'code': 'RUB'}},
        'description': 'Перевод организации',
        'from': 'Visa Classic 1596837868705199',
        'to': 'Visa Platinum 64686473678894779589'
    }

def test_operation_init(coll):
    example = Operation(coll)
    assert example.info == coll
    assert example.date == datetime.datetime.strptime(coll['date'], '%Y-%m-%dT%H:%M:%S.%f')
    assert example.description == coll['description']
    assert example.amount == coll['operationAmount']['amount']
    assert example.currency == coll['operationAmount']['currency']['name']
    assert example.from_card == []
    assert example.to_card == []

def test_operation_get_card_num(coll, coll_1):
    example = Operation(coll)
    example_1 = Operation(coll_1)
    assert example.get_card_num('from') == ['Visa Classic', '1596837868705199']
    assert example.get_card_num('to') == ['Счет', '64686473678894779589']
    assert example.get_card_num('aaa') == 'введено неверное значение'
    assert example_1.get_card_num('to') == ['Visa Platinum', '64686473678894779589']

def test_operation_hide_card_num(coll):
    example = Operation(coll)
    from_card = example.get_card_num('from')
    to_card = example.get_card_num('to')
    assert example.hide_card_num('from') == '1596 83** **** 5199'
    assert example.hide_card_num('to') == '**9589'
    assert example.hide_card_num('aaa') == 'введено неверное значение'

def test_display_info(coll):
    example = Operation(coll)
    from_card = example.get_card_num('from')
    to_card = example.get_card_num('to')
    assert example.display_info() == '''
        26.08.2019 Перевод организации
        Visa Classic 1596 83** **** 5199 -> Счет **9589
        31957.58 руб.'''


