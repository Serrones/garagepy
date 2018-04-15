import pprint

inventory = {
    'arrow': 10,
    'rope': 1,
    'knife': 5,
    'sword': 2,
    'apple': 10,
    'poison': 5,
    'medicine': 3
    }

dragon_loot = ['gold_coin', 'knife', 'gold_coin', 'gold_coin', 'ruby']


def display_inventory(inventory):
    total_item = 0
    for k, v in inventory.items():
        print(str(v) + ' - ' + k)
        total_item += 1
    print('Total items: ' + str(total_item))

def add_inventory(inventory, added_items):
    for loot in added_items:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    pprint.pprint(inventory)

display_inventory(inventory)

add_inventory(inventory, dragon_loot)

display_inventory(inventory)
