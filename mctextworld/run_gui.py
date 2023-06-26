from mctextworld.simulator import *

def print_candidate_actions(env):
    candidate_actions = env.action_lib.get_candidate_actions(env.state['inventory'])
    print("Candidate Actions: ", )
    index = 0 
    for action in candidate_actions:
        print(f"{index}: {action}")
        index += 1
    return candidate_actions

def get_input(env):
    # candidate_actions = print_candidate_actions(env)
    while True:
        candidate_actions = print_candidate_actions(env)
        user_input = input("Input the No. or name of the action: ")
        if user_input.isdigit():
            if int(user_input) < len(candidate_actions):
                action = candidate_actions[int(user_input)]
                break  
            else:
                print('Invalid Input!')
        else:
            if user_input in candidate_actions:
                action = user_input
                break
            else:
                print('Invalid Input!')
    return action

if __name__ == '__main__':
    print("Task: Obtain 1 diamond!")
    env = Env(
        init_inv = {'oak_log':3, 'cobblestone':8}, 
        task_obj = {'diamond': 1}
        )
    state, reward, done, info = env.reset()
    # print(f'env.state: {env.state}')
    # print(f'env.done: {env.done}')
    # print(f'env.check_item: {env.check_item(env.task_obj)}')
    for i in range(MAXIMUM_STEP):
        try:
            print(f"Step: {env.curr_step}/{MAXIMUM_STEP}")
            print(f"Inventory: {state['inventory']}")
            action = get_input(env)
            state, reward, done, info = env.step(action)
            # print("State: ", state)
            # print("Reward: ", reward)
            # print("Done: ", done)
            print("Info: ", info)
            print("#"*20)
            if done:
                print("Task Finished!")
                break
        except Exception as e:
            print(e)