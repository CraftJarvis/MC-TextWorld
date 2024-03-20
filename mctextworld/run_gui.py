from mctextworld.simulator import *
import argparse
import pytermgui as ptg
from pytermgui import Container,inline,tim,Window,Label,Button,Splitter,InputField

user_input = "not_changed_yet"

def quit():
    manager.close()

def on_click(bt):
    global window
    manager.remove(window)
    del window
    info_list = "Please choose your action"
    action=bt
    if action == None:
        info_list = ("Task Failed!")
        return
    obs, reward, done, info = env.step(action)
    if done:
        _, c = get_candidate_action(env, args.fix_action_space)
        obs_container = env.print_obs()
        window = Window(
            f"[bold blue]Task: {env.task_name}",
            f"Step: {env.curr_step}/{MAXIMUM_STEP}   Reward: {env.reward}",
            f"Done!",
            Button("Press Here to quit", onclick = lambda b:quit()),
            width=150
        )
        window.set_title(f"Task:{env.task_name}", postion="center")
        return
    
    elif (env.curr_step>=MAXIMUM_STEP):
        window = Window(
            f"[bold blue]Task: {env.task_name}",
            f"Step: {env.curr_step}/{MAXIMUM_STEP}   Reward: {env.reward}",
            f"Fail: Your steps are used up!",
            Button("Press Here to quit", onclick = lambda b:quit()),
            width=150
        )
        window.set_title(f"Task:{env.task_name}", postion="center")
        return
    
    _, c = get_candidate_action(env, args.fix_action_space)
    obs_container = env.print_obs()
    window = Window(
        f"[bold blue]Task: {env.task_name}",
        f"Step: {env.curr_step}/{MAXIMUM_STEP}   Reward: {env.reward}",
        obs_container,
        c,
        info_list,
        width=150
    )
    manager.add(window)
    return

def print_candidate_actions(action_lib, candidate_actions):
    content_list = []
    content_list.append(Label("[bold accent]Candidate Actions"))
    index = 0 
    type2act = {}
    for action in candidate_actions:
        type = action_lib[action][0]["type"]
        if type not in type2act:
            type2act[type] = []
        type2act[type].append(action)
    for type in type2act:
        
        #print("group: ", type)
        content_list.append(Label("[bold lightgreen]"+type))
        type2act[type] = sorted(type2act[type])
        action_list = []
        for action in type2act[type]:
                
            action_list.append(Button(f"{index}: {action}", onclick = lambda b: on_click(b.label.split(":")[1].strip())))
            candidate_actions[index] = action
            index += 1
        splitter_list = []
        while len(action_list)%3!=0:
            action_list.append(Label(" "))
        for i in range((len(action_list))//3):
            splitter_list.append(Splitter(action_list[i*3], action_list[i*3+1], action_list[i*3+2], separator=" "))
        
        content_list.extend(splitter_list)
    c = Container(*content_list, width=150)
    return candidate_actions, c

def get_candidate_action(env, fix_action_space):
    if(fix_action_space):
        candidate_actions = env.action_lib.all_actions
    else:
        candidate_actions = env.action_lib.get_candidate_actions(env.obs['inventory'])
    candidate_actions, c = print_candidate_actions(env.action_lib.action_lib, candidate_actions)
    return candidate_actions, c

def get_input(env, fix_action_space, plan_step=None):
    # candidate_actions = print_candidate_actions(env)
    while True:

        candidate_actions, _ = get_candidate_action(env, fix_action_space)
        
        global user_input
        if(plan_step is None):
            info_list = ["Choose the No. or Name of the action: "]
            #user_input = input()
        else:
            user_input = plan_step["type"]+"_"+plan_step["text"]
            #print("The agent 's choice: {}".format(user_input))
        
        action = None
        if user_input.isdigit():
            if int(user_input) < len(candidate_actions):
                action = candidate_actions[int(user_input)]
                break  
            else:
                info_list.append('\nInvalid Input!')
                if(plan_step is not None):
                    break
        else:
            if user_input in candidate_actions:
                action = user_input
                break
            else:
                info_list.append('\nInvalid Input!')
                if(plan_step is not None):
                    break
    return action, info_list

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
    
    if plan is not None:
        j = 0
        done = 0
        while j<len(plan):
            goal_reached = 1
            if "goal" in plan[j]:
                for item in plan[j]["goal"]:
                    if item not in env.obs["inventory"] or plan[j]["goal"][item]>env.obs["inventory"][item]:
                        goal_reached = 0
                        break
            j = j+goal_reached
            if(env.curr_step>=MAXIMUM_STEP):
                print("Fail: Your steps are used up!")
                break
            candidate_actions, _ = get_candidate_action(env, args.fix_action_space)
            action = plan[j]["type"]+"_"+plan[j]["text"]
            if action not in candidate_actions:
                print(f"Fail: invalid action:'{action}'")
            obs, reward, done, info = env.step(action)
            if done:
                print("Done!")
                break
        if not done:
            print("Fail: Plan Finished!")
            
    else:
        with ptg.WindowManager() as manager:
            step = 0
            _, c = get_candidate_action(env, args.fix_action_space)
            obs_container = env.print_obs()
            info_list = "Please choose your action"
            window = Window(
                f"[bold blue]Task: {env.task_name}",
                f"Step: {env.curr_step}/{MAXIMUM_STEP}   Reward: {env.reward}",
                obs_container,
                c,
                info_list,
                width=150
            )

            window.set_title(f"Task:{env.task_name}", position = 0)
            manager.add(window)
        

            