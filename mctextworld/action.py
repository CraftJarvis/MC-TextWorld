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

    def load_action_lib(self):
        with open(self.action_lib_path, 'r') as f:
            context = json.load(f)
        return dict(context)

    def check_action(self, inventory:dict, action:str):
        if action not in self.all_actions:
            return False, f"action {action} NOT exist!'"
            # raise Exception('action NOT in action space!')
        else:
            if not check_dict(inventory, self.action_lib[action]['precondition']):
                return False, f"invalid action {action} for not enough materials {' and '.join(list(self.action_lib[action]['precondition'].keys()))}!"
            elif not check_dict(inventory, self.action_lib[action]['tool']):
                return False, f"invalid action {action} for not having tool {' and '.join(list(self.action_lib[action]['tool'].keys()))}!"
            # candidate_actions = self.get_candidate_actions(inventory)
            # if action not in candidate_actions:
            #     # raise Exception('invalid action!')
            #     return False, 'invalid action for not enough materials or tools!'
            else: 
                return True, 'valid action.'

    def get_candidate_actions(self, inventory:dict):
        candidate_actions = []
        for action in self.all_actions:
            if check_dict(inventory, self.action_lib[action]['precondition']) and check_dict(inventory, self.action_lib[action]['tool']):
                candidate_actions.append(action)
        return candidate_actions
    

