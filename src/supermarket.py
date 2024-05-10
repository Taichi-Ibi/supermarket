import json

with open("item/item.json") as f:
    item_list = json.load(f)

def non_taxed_price(orders):
    price = 0
    for order in orders:
        price += item_list.get(str(order["id"])).get('金額')*order["amount"]
    return price

def taxed_price(orders):
    price = non_taxed_price(orders)
    discount_price = discount(orders)
    return round((price - discount_price) * 1.08)

def total_price(orders):
    tabaco_ids = [6, 7]
    non_taxed_orders = [order for order in orders if order["id"] in tabaco_ids]
    taxed_orders = [order for order in orders if order["id"] not in tabaco_ids]
    return taxed_price(taxed_orders) + non_taxed_price(non_taxed_orders)

def discount(orders):
    apple_ids = [1]
    apple_orders = [order for order in orders if order["id"] in apple_ids]
    count = 0
    for order in apple_orders:
        count += order["amount"]
    return (count // 3) * 20
