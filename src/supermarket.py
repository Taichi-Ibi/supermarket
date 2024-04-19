import json

with open("../item/item.json") as f:
    item_list = json.load(f)

order = [[7, 5], [2, 11], [8, 8]]

def item_price(item_num, amount):
    return item_list.get(str(item_num)).get('金額')*amount

def in_tax(total_price):
    return total_price*1.08

def unit_price(order):
    p = []
    for i in order:
        p.append(item_price(*i))
    return in_tax(sum(p))

print(unit_price(order))