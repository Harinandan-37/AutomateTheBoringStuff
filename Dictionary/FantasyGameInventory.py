import copy
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    count = 0
    print("Inventory: ")
    for item, number in inventory.items():
        print()
        print(str(number) + ' ' + item)
        count += int(number)
    print()
    print("Total number of items: %d" % (count))

# displayInventory(stuff)

#########################################################################

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    lootList = [*set(addedItems)] #remove duplicates
    newinv = copy.deepcopy(inventory)
    for item, number in inventory.items():
        for loot in lootList:       
            #finding number of existing elements
            lootCount = addedItems.count(loot)    
                 
            if loot == item:
                #update existing items numbers
                newinv[item] += lootCount

            if loot not in inventory:
                newinv.setdefault(loot,str(lootCount)) #add the item if not in dict
            lootCount = 1

    inventory = copy.copy(newinv)
    return inventory

x = addToInventory(inv,dragonLoot) 

displayInventory(x)