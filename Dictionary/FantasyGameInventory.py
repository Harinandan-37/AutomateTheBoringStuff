stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    count = 0
    print("Inventory: ")
    for item, number in inventory.items():
        print()
        print(str(number) + ' ' + item)
        count += int(number)
    print()
    print("Total number of items: %d" % (count))

displayInventory(stuff)

    
