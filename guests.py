all_guests = {
    'Alice': {'apples': 5, 'pretzels': 3},
    'Bob': {'ham sandwichs': 4, 'apples': 2},
    'Carol': {'cups': 10, 'apple pies': 1},
    'Louis': {'plates': 5, 'juice': 1},
    'Joseph': {'apples': 3, 'biscuits': 5, 'cups': 6}
}

def picnic_list(guests, item):
    total_num = 0
    for guest, i in guests.items():
        total_num = total_num + i.get(item, 0)
    return total_num

print('Number of things being brought:')
print(' - Apples        ' + str(picnic_list(all_guests, 'apples')))
print(' - Pretzels      ' + str(picnic_list(all_guests, 'pretzels')))
print(' - Ham Sandwichs ' + str(picnic_list(all_guests, 'ham_sandwichs')))
print(' - Cups          ' + str(picnic_list(all_guests, 'cups')))
print(' - Apple Pies    ' + str(picnic_list(all_guests, 'apple pies')))
print(' - Plates        ' + str(picnic_list(all_guests, 'plates')))
print(' - Juice         ' + str(picnic_list(all_guests, 'juice')))
print(' - Biscuits      ' + str(picnic_list(all_guests, 'biscuits')))
