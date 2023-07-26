import os
import json

from mctextworld.utils import *

class ActionLibrary:
    '''
    ActionLibrary: This is a action library for test the online planner in Minecraft.
    "mine_log": {
        "output": {"log": 1},
        "type": "mine",
        "precondition": {},
        "tool": {}
    }
    '''
    def __init__(self):
        basepath = os.path.abspath(__file__)
        folder = os.path.dirname(basepath)
        data_path = os.path.join(folder, 'action_lib.json')
        
        self.action_lib_path = data_path
        self.action_lib = self.load_action_lib()
        self.all_actions = list(self.action_lib.keys())

        print(f"Action Library: {len(self.all_actions)}") # 732
        print(f"Action Library: {len(set(self.all_actions))}") # 732

    def load_action_lib(self):
        with open(self.action_lib_path, 'r') as f:
            context = json.load(f)
        return dict(context)

    def check_action(self, inventory:dict, action:str):
        if action not in self.all_actions:
            return False, f"action {action} NOT exist!'"
            # raise Exception('action NOT in action space!')
        else:
            for act in self.action_lib[action]:
                # if not check_dict(inventory, self.action_lib[action]['precondition']):
                #     return False, f"invalid action {action} for not enough materials {' and '.join(list(self.action_lib[action]['precondition'].keys()))}!"
                # elif not check_dict(inventory, self.action_lib[action]['tool']):
                #     return False, f"invalid action {action} for not having tool {' and '.join(list(self.action_lib[action]['tool'].keys()))}!"
                # # candidate_actions = self.get_candidate_actions(inventory)
                # # if action not in candidate_actions:
                # #     # raise Exception('invalid action!')
                # #     return False, 'invalid action for not enough materials or tools!'
                # else: 
                #     return True, 'valid action.'
                if check_dict(inventory, act['precondition']) and check_dict(inventory, act['tool']):
                    return act, 'valid action.'
                # if not check_dict(inventory, act):
                #     return False, f"invalid action {action} for not enough materials {' and '.join(list(self.action_lib[action]['precondition'].keys()))}!"
                # elif not check_dict(inventory, self.action_lib[action]['tool']):
                #     return False, f"invalid action {action} for not having tool {' and '.join(list(self.action_lib[action]['tool'].keys()))}!"
                # else: 
                #     return True, 'valid action.'
            return False, 'unvalid action!'

    def get_candidate_actions(self, inventory:dict):
        candidate_actions = []
        for action in self.all_actions:
            # print(f"action: {action}")
            # print(f"action details: {self.action_lib[action]}")
            for cand_action in self.action_lib[action]:
                if check_dict(inventory, cand_action['precondition']) and check_dict(inventory, cand_action['tool']):
                    candidate_actions.append(action)
        return candidate_actions
    

