
# check if all items in inventory
def check_dict(inventory:dict, item:dict):
    for i in item.keys():
        if i in inventory.keys(): # check item exist
            if item[i] > inventory[i]: # check item enough
                return False
        else:
            return False
    return True


