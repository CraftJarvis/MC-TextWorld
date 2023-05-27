'''
Visit the https://mermaid.live/ page to see the graph
'''

import json

with open('goal_lib.json', 'r') as f:
    goal_lib = json.load(f)

f = open('graph_mermaid.txt', 'w') 
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


