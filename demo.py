import json 

with open('mctextworld/action_lib.json', 'r') as f:
    action_lib = json.load(f)

def output2string(dct:dict):
    returnStr = ' and '.join(list(cand_action['output']))
    return returnStr

def tool2string(dct:dict):
    returnStr = ' and '.join(list(cand_action['tool']))
    if returnStr == '':
        returnStr = 'without tool'
    else:
        returnStr = 'with ' + returnStr
    return returnStr

def materials2string(dct:dict):
    returnStr = " and ".join(list(cand_action['precondition']))
    if returnStr == '':
        pass
    else:
        returnStr = 'from ' + returnStr
    return returnStr

for act in action_lib:
    print(f"act: {act}")
    print(f"act details: {action_lib[act]}")
    for cand_action in action_lib[act]:
        print(f"cand_action: {cand_action}")
        print(f"action_abbr: {cand_action['type']} {output2string(cand_action['output'])} {materials2string(cand_action['precondition'])} {tool2string(cand_action['tool'])}")
    print("#"*20)

