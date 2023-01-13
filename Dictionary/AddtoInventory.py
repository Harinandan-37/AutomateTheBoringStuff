inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print (dragonLoot.count('gold coin'))

def addToInventory(inventory, addedItems):
    for item, number in inventory.items():
        itemCount = number
        for loot in dragonLoot:
            lootCount = 0
            
            lootCount += 1
                    
            if loot == item:
                itemCount += 1 #update existing items numbers
                
            else:
                inventory.setdefault(loot,str(lootCount)) #add the item if not in dict
            lootCount = 1

addToInventory(inv,dragonLoot)

                
        

