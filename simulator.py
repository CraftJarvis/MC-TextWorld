import json

MAXIMUM_STEP = 100

class Env:
    '''
    Minecraft Simulator: This is a simulator for test the online planner in Minecraft.
    '''
    def __init__(self, init_inv = {}, task_obj = {}):
        self.init_inv = init_inv
        self.legal_actions = ["mine", "craft", "smelt"]
        self.task_obj = task_obj

        self.reset()
        
    def reset(self):
        self.state = {
            'inventory': self.init_inv
        }
        self.reward = 0
        self.done = False
        self.info = {}
        self.curr_step = 0

    # check the action is valid or not
    def check_action(self, action):
        # assert action in ["mine", "craft", "smelt"]
        pass

    def run_action(self, action):
        if action == "mine":
            pass
        elif action == "craft":
            pass
        elif action == "smelt":
            pass
        else:
            action = no_op()

    def step(self, action):
        '''
        return next state, reward, done, info
        '''
        self.check_action(action)
        self.curr_step += 1
        

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

class Agent:
    '''
    Agent: This is a agent for test the online planner in Minecraft.
    '''
    def __init__(self):
        pass

    def parse_action(self):
        pass

    def parse_goal(self):
        pass

class DEPS_Agent(Agent):
    '''
    DEPS_Agent: This is a agent for test the online planner in Minecraft.
    '''
    def __init__(self):
        pass
    
if __name__ == '__main__':
    env = Env(
        init_inv = {'log':3, 'planks': 4, }, 
        task_obj = {'planks': 1, 'log':5}
        )
    print(f'env.state: {env.state}')
    print(f'env.done: {env.done}')
    print(f'env.check_item: {env.check_item(env.task_obj)}')
