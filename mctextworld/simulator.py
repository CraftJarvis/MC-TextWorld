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
    def __init__(self, init_inv = {}, task_obj = {}):
        self.init_inv = init_inv
        self.legal_actions = ["mine", "craft", "smelt"]
        self.task_obj = task_obj

        # self.goal_lib = self.load_goal_lib()
        self.action_lib = ActionLibrary()

        self.reset()

    def reset(self):
        self.state = {
            'inventory': copy.deepcopy(self.init_inv)
        }
        self.reward = 0
        self.done = False
        self.info = {}
        
        self.curr_step = 0
        self.executed_actions = []

        # return self.state # observation?
        return self.state, self.reward, self.done, self.info

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
        return next state, reward, done, info
        '''
        # Check action validation
        res, msg = self.action_lib.check_action(self.state['inventory'], action)
        self.curr_step += 1

        self.executed_actions.append(action)

        if not res:
            return self.state, self.reward, self.done, {'action success': res, 'message': msg}

        output = self.action_lib.action_lib[action]['output'] # effect 
        precondition = self.action_lib.action_lib[action]['precondition'] # precondition

        # delete precondition items
        for key, val in precondition.items():
            self.state['inventory'][key] -= val
        
        # add output items
        for key, val in output.items():
            if key in self.state['inventory'].keys():
                self.state['inventory'][key] += val
            else:
                self.state['inventory'][key] = val
        
        self.done = self.check_done(inventory = self.state['inventory'])
        inventory = self.check_inventory(inventory = self.state['inventory'])

        return self.state, self.reward, self.done, {'action success': True}

    # def check_item(self, item:str):
    #     if item in self.state['inventory'].keys():
    #         return True
    #     else:
    #         return False
    
    # def check_item(self, item:dict):
    #     for i in item.keys():
    #         if i in self.state['inventory'].keys(): # check item exist
    #             if item[i] > self.state['inventory'][i]: # check item enough
    #                 return False
    #         else:
    #             return False
    #     return True
    
if __name__ == '__main__':
    env = Env(
        init_inv = {}, 
        task_obj = {'diamond': 1, 'log': 3}
        )
    # print(f'env.state: {env.state}')
    # print(f'env.done: {env.done}')
    # print(f'env.check_item: {env.check_item(env.task_obj)}')
    # for i in range(MAXIMUM_STEP):
    #     try:
    #         print("Step: ", env.curr_step)
    #         print("Candidate Actions: ", env.action_lib.get_candidate_actions(env.state['inventory']))
    #         action = input("Action: ")
    #         state, reward, done, info = env.step(action)
    #         print("State: ", state)
    #         print("Reward: ", reward)
    #         print("Done: ", done)
    #         print("Info: ", info)
    #         print("#"*20)
    #         if done:
    #             print("Task Finished!")
    #             break
    #     except Exception as e:
    #         print(e)