import json
import os
import copy

import gym
from gym import spaces
from gym.utils import seeding

from mctextworld.action import ActionLibrary
from mctextworld.utils import *

MAXIMUM_STEP = 100

# prefix = os.getcwd()
# action_lib_path = os.path.join(prefix, 'action_lib.json')

class Env(gym.Env):
    '''
    Minecraft Simulator: This is a simulator for test the online planner in Minecraft.
    '''
    def __init__(self,task_name = "Obtain 1 diamond", init_inv = {}, task_obj = {}, biome = "plains"):
        self.task_name = task_name
        self.init_inv = init_inv
        self.legal_actions = ["mine", "craft", "smelt"]
        self.task_obj = task_obj
        self.reward = 0
        # self.goal_lib = self.load_goal_lib()
        self.action_lib = ActionLibrary()
        self.obs = {
            "inventory": copy.deepcopy(self.init_inv),
            "position": [0,0,0],
            "biome": biome,
        }
        self.reset()
        
    # def load_goal_lib(self):
    #     with open(goal_lib_path, 'r') as f:
    #         context = json.load(f)
    #     return dict(context)
    
    def print_obs(self):
        print("CURRENT STATE:")
        print("-----------------------------")
        print("Inventory: ", self.obs['inventory'])
        print("position: ", self.obs['position'])
        print("biome: ", self.obs['biome'])
        print("Reward: ", self.reward)
        print("Done: ", self.done)
        print("Info: ", self.info)
        print("-----------------------------")

    def reset(self):
        self.obs = {
            "inventory": copy.deepcopy(self.init_inv),
            "position": [0,0,0],
            "biome": "plains",
        }
        self.reward = 0
        self.done = False
        self.info = {}
        
        self.curr_step = 0
        self.executed_actions = []

        # return self.obs # observation?
        return self.obs, self.reward, self.done, self.info

    # # check the action is valid or not
    # def check_action(self, action):
    #     # assert action in ["mine", "craft", "smelt"]
    #     if action not in self.goal_lib:
    #         raise Exception('Invalid action!')
    #     pass

    # def run_action(self, action):
    #     if action == "mine":
    #         pass
    #     elif action == "craft":
    #         pass
    #     elif action == "smelt":
    #         pass
    #     else:
    #         # action = no_op()
    #         pass

    def check_done(self, inventory):
        if check_dict(inventory, self.task_obj):
            return True
        else:
            return False

    def check_inventory(self, inventory):
        new_inventory = {}
        for key, val in inventory.items():
            if val < 0:
                raise Exception('Invalid inventory!')
            elif val > 0:
                new_inventory[key] = val
            else:
                pass
        return inventory

    def step(self, action: str):
        '''
        return next obs, reward, done, info
        '''
        # Check action validation
        act, msg = self.action_lib.check_action(self.obs['inventory'], action)
        self.curr_step += 1

        self.executed_actions.append(act)

        if not act:
            return self.obs, self.reward, self.done, {'action success': False, 'message': msg}

        # output = self.action_lib.action_lib[action]['output'] # effect 
        # precondition = self.action_lib.action_lib[action]['precondition'] # precondition
        output = act['output'] # effect 
        precondition = act['precondition'] # precondition

        # delete precondition items
        for key, val in precondition.items():
            self.obs['inventory'][key] -= val
        
        # add output items
        for key, val in output.items():
            if key in self.obs['inventory'].keys():
                self.obs['inventory'][key] += val
            else:
                self.obs['inventory'][key] = val
        
        self.done = self.check_done(inventory = self.obs['inventory'])
        inventory = self.check_inventory(inventory = self.obs['inventory'])

        return self.obs, self.reward, self.done, {'action success': True}
    
if __name__ == '__main__':
    env = Env(
        init_inv = {}, 
        task_obj = {'diamond': 1, 'log': 3}
        )
