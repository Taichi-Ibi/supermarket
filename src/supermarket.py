import json

with open("item/item.json") as f:
    item_list = json.load(f)

def non_taxed_price(orders):
    price = 0
    for order in orders:
        price += item_list.get(str(order["id"])).get('金額')*order["amount"]
    return price

def taxed_price(orders):
    return round(non_taxed_price(orders)*1.08)

def item_price(item_num, amount):
    if item_num == 1 and amount >= 3:
        price = 280 * (amount // 3) + 100 * (amount % 3)
    else:
        price = item_list.get(str(item_num)).get('金額')*amount
    return price

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
    
    return round(tabaco_price(t) + unit_price(other))

