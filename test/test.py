from src.supermarket import item_price, tabaco_price, unit_price

#お題4
order = [[1, 4]]
y_pred = item_price(*order[0])
y_true = 380
assert y_pred == y_true, f'y_pred:{y_pred}, y_true:{y_true}'

order = [[1, 2]]
y_pred = item_price(*order[0])
y_true = 200
assert y_pred == y_true, f'y_pred:{y_pred}, y_true:{y_true}'

#お題3
order = [[6, 1]]
y_pred = tabaco_price(order)
y_true = 420
assert y_pred == y_true, f'y_pred:{y_pred}, y_true:{y_true}'

order = [[7, 1]]
y_pred = tabaco_price(order)
y_true = 440
assert y_pred == y_true, f'y_pred:{y_pred}, y_true:{y_true}'

#お題2
order = [[2, 1], [3, 1]]
y_pred = unit_price(order)
y_true = 190 * 1.08
assert y_pred == y_true, f'y_pred:{y_pred}, y_true:{y_true}'

# #お題1
# order = [[2, 1], [3, 1]]
# y_pred = unit_price(order)
# y_true = 190 * 1.08
# assert y_pred == y_true, f'y_pred:{y_pred}, y_true:{y_true}'
