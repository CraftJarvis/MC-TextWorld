import json
# check if all items in inventory
def check_dict(inventory:dict, item:dict):
    for i in item.keys():
        if i in inventory.keys(): # check item exist
            if item[i] > inventory[i]: # check item enough
                return False
        else:
            return False
    return True

# add group to action
def add_group_to_action(old_path, path):
    with open(old_path, 'r') as j:
        old_action_lib = json.load(j)
    new_action_lib = {}
    for action in old_action_lib.keys():
        new_action_lib[action] = []
        for cand_action in old_action_lib[action]:
            cand_action['group'] = action.split("_")[0]
            new_action_lib[action].append(cand_action)
    with open(path, 'w') as j:
        json.dump(new_action_lib, j)
        
def create_task_json(old_path, path):
    with open(old_path, 'r') as j:
        old_task_lib = json.load(j)
    new_task_lib = []
    for task in old_task_lib:
        task["description"] = "Obtain a " + task["task"].replace("_", " ")
        new_task_lib.append(task)
    with open(path, 'w') as j:
        json.dump(old_task_lib, j)
        
create_task_json("jarvis_task.json", "tasks.json")