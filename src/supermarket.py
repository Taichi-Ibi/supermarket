import json

with open("../item/item.json") as f:
    item_list = json.load(f)

# print(item_list[0].get("商品番号"))
# print(item_list[0].get("商品名"))
# print(item_list[0].get("金額"))

def unit_price(item_num):
    return item_list.get(str(item_num)).get('金額')

print(unit_price(6))