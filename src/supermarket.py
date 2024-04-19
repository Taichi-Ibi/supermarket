import json

with open("../item/item.json") as f:
    item_list = json.load(f)

order = [[7, 1], [1, 5], [6, 1]]

def item_price(item_num, amount):
    return item_list.get(str(item_num)).get('金額')*amount

def in_tax(total_price):
    return total_price*1.08

def unit_price(order):
    p = []
    for i in order:
        p.append(item_price(*i))
    return in_tax(sum(p))

def tabaco_price(order):
    p = []
    for i in order:
        p.append(item_price(*i))
    return sum(p)

def total_price(order):
    t = []
    other = []

    for n in order:
        if n[0] == 6:
            t.append(n)
        elif n[0] == 7:
            t.append(n)
        else:
            other.append(n)
    
    return tabaco_price(t) + unit_price(other)

print(total_price(order))