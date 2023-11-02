import gradio as gr
import random
import time

from mctextworld.simulator import *

title = "Minecraft TextWorld"
description = "Welcome to a text-based world that simulates the rules of Minecraft. In this interactive environment, you can select actions to engage with the virtual world and accomplish various tasks."

env = Env(
    init_inv = {}, 
    task_obj = {'diamond': 1}
    )
state, reward, done, info = env.reset()

def get_candidate_actions(env):
    candidate_actions = env.action_lib.get_candidate_actions(env.state['inventory'])
    print("Candidate Actions: ", )
    index = 0 
    for action in candidate_actions:
        print(f"{index}: {action}")
        index += 1
    return candidate_actions

def get_env_response(env, message):
    # check action is valid or not 
    candidate_actions = env.action_lib.get_candidate_actions(env.state['inventory'])
    if message.isdigit():
        if int(message) < len(candidate_actions):
            action = candidate_actions[int(message)]
        else:
            return "Invalid Input! Choose optional actions!"
    else:
        if message in candidate_actions:
            action = message
        else:
            return "Invalid Input! Choose optional actions!"

    # run this action
    state, reward, done, info = env.step(action)
    if info['reach_maximum_step']:
        return "Reach maximum step! Game Over!"
    return_msg = f"Run action [{action}] successfully.\n"
    return_msg += f"Current step: {env.curr_step}/{env.maximum_step}\n"
    return_msg += f"Current state: {state}\n"
    return_msg += f"Current candidate actions:\n"
    for i,act in enumerate(candidate_actions):
        return_msg += f"[{i}]: {act}\n"
    return return_msg


def random_generation(message, chat_history):
    # bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
    bot_message = get_env_response(env, message)
    chat_history.append((message, bot_message))
    # time.sleep(2)
    return "", chat_history

with gr.Blocks(theme = "gradio/base") as demo:
    tit = gr.Markdown(f"<h1 style='text-align: center; margin-bottom: 1rem'>{title}</h1>")
    desc = gr.Markdown(description)
    chatbot = gr.Chatbot(
        value=[[None, f"Current Task: {env.task_obj}\n"+get_env_response(env, "no_op")]],
        height = 600
        )
    # textbox = gr.Textbox()
    with gr.Row():
        msg = gr.Textbox(
                container=False,
                show_label=False,
                label="Message",
                placeholder="Type a message...",
                scale=7,
                autofocus = True
                )
        submit_btn = gr.Button(
                    "Submit",
                    variant="primary",
                    scale=1,
                    min_width=100,
                )
    clear = gr.ClearButton([msg, chatbot])

    state = gr.State()

    msg.submit(random_generation, [msg, chatbot], [msg, chatbot])
    submit_btn.click(random_generation,  
                 inputs=[msg, chatbot], 
                 outputs=[msg, chatbot]) 

if __name__ == "__main__":
    demo.launch()


