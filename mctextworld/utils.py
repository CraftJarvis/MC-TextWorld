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

def generate_mermaid(input_file: str = 'action_lib.json', output_file: str = 'graph_mermaid.txt'):
    '''
    Visit the https://mermaid.live/ page to see the graph
    '''
    with open(input_file, 'r') as f:
        goal_lib = json.load(f)

    f = open(output_file, 'w') 
    f.write("graph TD\n")

    for key in goal_lib.keys():
        action = goal_lib[key]
        output_item = list(action['output'].keys())[0]
        # print(output_item)
        precondition = list(action['precondition'].keys())
        if len(precondition) > 0:
            # print("&".join(precondition))
            print(f"  {output_item} --> {'&'.join(precondition)}")
            f.write(f"  {output_item} --> {'&'.join(precondition)}\n")

        tool = list(action['tool'].keys())
        if len(tool) > 0:
            # print("&".join(tool))
            print(f"  {output_item} --> {'&'.join(tool)}")
            f.write(f"  {output_item} --> {'&'.join(tool)}\n")

    f.close()


