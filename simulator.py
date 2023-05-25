import json
import os
import copy

import gym
from gym import spaces
from gym.utils import seeding

MAXIMUM_STEP = 100

prefix = os.getcwd()
goal_lib_path = os.path.join(prefix, 'goal_lib.json')

class Env(gym.Env):
    '''
    Minecraft Simulator: This is a simulator for test the online planner in Minecraft.
    '''
    def __init__(self, init_inv = {}, task_obj = {}):
        self.init_inv = init_inv
        self.legal_actions = ["mine", "craft", "smelt"]
        self.task_obj = task_obj

        self.goal_lib = self.load_goal_lib()

        self.reset()
        
    def load_goal_lib(self):
        with open(goal_lib_path, 'r') as f:
            context = json.load(f)
        return dict(context)

    def reset(self):
        self.state = {
            'inventory': copy.deepcopy(self.init_inv)
        }
        self.reward = 0
        self.done = False
        self.info = {}
        self.curr_step = 0

        return self.state # observation?

    # check the action is valid or not
    def check_action(self, action):
        # assert action in ["mine", "craft", "smelt"]
        if action not in self.goal_lib:
            raise Exception('Invalid action!')
        pass

    def run_action(self, action):
        if action == "mine":
            pass
        elif action == "craft":
            pass
        elif action == "smelt":
            pass
        else:
            # action = no_op()
            pass

    def step(self, action: str):
        '''
        return next state, reward, done, info
        '''
        # Check action validation
        self.check_action(action)
        self.curr_step += 1

        # Check action preconditions
        pre_flag = True
        goal = self.goal_lib[action]
        for key, val in goal['precondition'].items():
            if key not in self.state['inventory']:
                pre_flag = False
                break
            if self.state['inventory'][key] < val:
                pre_flag = False
                break
        for key, val in goal['tool'].items():
            if key not in self.state['inventory']:
                pre_flag = False
                break
            if self.state['inventory'][key] < val:
                pre_flag = False
                break
        
        if not pre_flag:
            return self.state, 0, self.done, {'success': False}

        # Execute action
        for key, val in goal['precondition'].items():
            self.state['inventory'][key] -= val
            if self.state['inventory'][key] == 0:
                del self.state['inventory'][key]
        for key, val in goal['output'].items():
            if key not in self.state['inventory']:
                self.state['inventory'][key] = 0
            self.state['inventory'][key] += val

        # Check if the task is done
        is_done = True
        for key, val in self.task_obj.items():
            if key not in self.state['inventory']:
                is_done = False
                break
            if self.state['inventory'][key] < val:
                is_done = False
                break
        if is_done:
            self.done = True

        return self.state, 0, self.done, {'success': True}

    # def check_item(self, item:str):
    #     if item in self.state['inventory'].keys():
    #         return True
    #     else:
    #         return False
    
    def check_item(self, item:dict):
        for i in item.keys():
            if i in self.state['inventory'].keys(): # check item exist
                if item[i] > self.state['inventory'][i]: # check item enough
                    return False
            else:
                return False
        return True
    
if __name__ == '__main__':
    env = Env(
        init_inv = {'log':3, 'planks': 4, }, 
        task_obj = {'planks': 1, 'log':5}
        )
    print(f'env.state: {env.state}')
    print(f'env.done: {env.done}')
    print(f'env.check_item: {env.check_item(env.task_obj)}')