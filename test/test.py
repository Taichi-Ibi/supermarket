import pytest
from src.supermarket import item_price, tabaco_price, unit_price, non_taxed_price

#お題1
@pytest.mark.parametrize("test_input, expected", [
    ([{"id":2, "amount":1}, {"id":3, "amount":1}], 190)
])
def test_q1(test_input, expected):
    y_pred = non_taxed_price(test_input)
    assert y_pred == expected

# @pytest.mark.parametrize("test_input, expected", [
#     ([[2, 1], [3, 1]], 190)
# ])
# def test_q1(test_input, expected):
#     y_pred = non_taxed_price(test_input)
#     assert y_pred == expected, f'y_pred:{y_pred}, y_true:{expected}'

#お題2
@pytest.mark.parametrize("test_input, expected", [
    ([[2, 1], [3, 1]], 190 * 1.08)
])
def test_q2(test_input, expected):
    y_pred = unit_price(test_input)
    assert y_pred == expected, f'y_pred:{y_pred}, y_true:{expected}'

#お題3
@pytest.mark.parametrize("test_input, expected", [
    ([[6, 1]], 420),
    ([[7, 1]], 440)
])
def test_q3(test_input, expected):
    y_pred = tabaco_price(test_input)
    assert y_pred == expected, f'y_pred:{y_pred}, y_true:{expected}'

#お題4
@pytest.mark.parametrize("test_input, expected", [
    ([[1, 4]], 380),
    ([[1, 2]], 200)
])
def test_q4(test_input, expected):
    y_pred = item_price(*test_input[0])
    assert y_pred == expected, f'y_pred:{y_pred}, y_true:{expected}'