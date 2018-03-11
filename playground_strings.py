"""
String manipulations

"""


def print_food_list(itemsDict, leftWidth, rightWidth):
    print('Food For Today'.center(leftWidth + rightWidth, '-'))
    for food, price in itemsDict.items():
        print(food.ljust(leftWidth, '.') + str(price).rjust(rightWidth))


food_dict = {
            'banana': 5,
            'avocado': 4.50,
            'ananas': 3.75,
            'lettuce': 2.25,
            'watermelon': 7.50,
}

print_food_list(food_dict, 15, 5)
print_food_list(food_dict, 20, 7)
