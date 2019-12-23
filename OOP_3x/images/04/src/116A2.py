#162A-2
item_type = "widget"
inv = Inventory()
inv.lock(item.type)
try:
    num_left = inv.purchase(item_type)
except InvalidItemType:
    print("sorry, the item you requested {}".format(item_type))
except OutOfStock:
    print("not available")
else:
    print("Purchase is complete. There are {num_lef} {item_left} {item_type}s left")
finally:
    inv.unlock(item_type)
