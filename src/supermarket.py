import json

with open("../item/item.json") as f:
    item_list = json.load(f)

def unit_price(item_num):
    p = []
    for i in item_num:
        p.append(item_list.get(str(i)).get('金額'))
    return sum(p)

print(unit_price([9,4,6]))