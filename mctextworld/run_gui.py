from mctextworld.simulator import *
import argparse
def print_candidate_actions(action_lib, candidate_actions):
    print("Candidate Actions: ", )
    index = 0 
    type2act = {}
    for action in candidate_actions:
        type = action_lib[action][0]["type"]
        if type not in type2act:
            type2act[type] = []
        type2act[type].append(action)
    for type in type2act:
        
        print("---------------")
        print("group: ", type)
        type2act[type] = sorted(type2act[type])
        print("| ", end="")
        for action in type2act[type]:
            print(f"{index}: {action}", end=" | ")
            candidate_actions[index] = action
            index += 1
        print("")
    return candidate_actions

def get_input(env, fix_action_space, plan_step=None):
    # candidate_actions = print_candidate_actions(env)
    while True:
        if(fix_action_space):
            candidate_actions = env.action_lib.all_actions
        else:
            candidate_actions = env.action_lib.get_candidate_actions(env.obs['inventory'])
        candidate_actions = print_candidate_actions(env.action_lib.action_lib, candidate_actions)
        
        if(plan_step is None):
            user_input = input("Choose the No. or Name of the action: ")
        else:
            user_input = plan_step["type"]+"_"+plan_step["text"]
            print("The agent 's choice: {}".format(user_input))
        
        action = None
        if user_input.isdigit():
            if int(user_input) < len(candidate_actions):
                action = candidate_actions[int(user_input)]
                break  
            else:
                print('Invalid Input!')
                if(plan_step is not None):
                    break
        else:
            if user_input in candidate_actions:
                action = user_input
                break
            else:
                print('Invalid Input!')
                if(plan_step is not None):
                    break
    return action

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--fix_action_space', action='store_true', help='Fix the action space.')
    parser.add_argument('--task_name', type=str, default='diamond_pickaxe', help='Task Name which should be in the tasks.json')
    parser.add_argument('--use_plan', action = 'store_true', help='Use the plan to guide the action selection. The task name should be a key in the plans.json')
    args = parser.parse_args()
    
    with open("tasks.json", "r") as j:
        jarvis_task = json.load(j)
    task_setting = None
    for t in jarvis_task:
        if t["task"]==args.task_name:
            task_setting = t
            break
    if(task_setting is None):
        raise ValueError("Task Not Found!")
    
    print("Task: {}!".format(task_setting['description']))
    env = Env(
        task_name = task_setting["description"],
        init_inv = task_setting["env"]["init_inventory"], 
        task_obj = task_setting["task_obj"]
        )
    obs, reward, done, info = env.reset()
    
    plan = None
    if(args.use_plan):
        with open("plans.json", "r") as j:
            plans = json.load(j) 
        plan = plans[args.task_name]
    
    j = 0
    for i in range(MAXIMUM_STEP):
        
        print(f"\n\n\n\nTask:{env.task_name}   Step: {env.curr_step}/{MAXIMUM_STEP}   Reward: {env.reward}")
        print("")
        env.print_obs()
        print("")
        
        if plan is not None:
            goal_reached = 1
            if "goal" in plan[j]:
                for item in plan[j]["goal"]:
                    if item not in env.obs["inventory"] or plan[j]["goal"][item]>env.obs["inventory"][item]:
                        goal_reached = 0
                        break
            j = j+goal_reached
            if(j>=len(plan)):
                print("Task Failed!")
                break
            action = get_input(env, args.fix_action_space, plan[j])
        else:
            action = get_input(env, args.fix_action_space)
            
        if action == None:
            print("Task Failed!")
            break
        obs, reward, done, info = env.step(action)
        if done:
            print("\n\n\n\n")
            env.print_obs()
            print("Task Finished!")
            break