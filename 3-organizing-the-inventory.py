inventory = [
    {"name": 'doll', "quantity": 5, "category": 'toys'},
    {"name": 'car', "quantity": 3, "category": 'toys'},
    {"name": 'ball', "quantity": 2, "category": 'sports'},
    {"name": 'car', "quantity": 2, "category": 'toys'},
    {"name": 'racket', "quantity": 4, "category": 'sports'}
]


def organizeInventory(inventory):
    inventory_dict = {}
    for item in inventory:
        if item["category"] not in inventory_dict:
            inventory_dict[item["category"]] = {}

        if item["name"] not in inventory_dict[item["category"]]:
            inventory_dict[item["category"]][item["name"]] = item["quantity"]
        else:
            inventory_dict[item["category"]][item["name"]] += item["quantity"]

    return inventory_dict


organizeInventory(inventory)
