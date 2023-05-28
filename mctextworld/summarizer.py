import json
import os
import openai
import time

import copy

class Summarizer():
    def __init__(self):
        prefix = os.getcwd()
        self.openai_keys_path = os.path.join(prefix, '../data/openai_keys.txt')
        self.summarize_prompt_path = os.path.join(prefix, '../data/summarize_prompt.json')

        self.openai_keys = self.load_openai_keys()
        self.summarize_prompt = self.load_summarize_prompt()
        
        self.dialogue = eval(self.summarize_prompt)

    def load_openai_keys(self, ):
        with open(self.openai_keys_path, 'r') as f:
            context = f.read()
        return context.split('\n')

    def load_summarize_prompt(self, ):
        with open(self.summarize_prompt_path, 'r') as f:
            context = json.load(f)
        return str(context)
    
    def update_key(self, ):
        curr_key = self.openai_keys[0]
        openai.api_key = curr_key
        self.openai_keys.remove(curr_key)
        self.openai_keys.append(curr_key)

    def query_gpt3(self, msg):
        server_flag = 0
        server_cnt = 0
        response = ''
        # print('prompt_text length:', len(msg))
        # prompt_text = prompt_text[-4000:]
        while server_cnt < 10:
            try:
                self.update_key()
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=msg,
                    temperature=0,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                # print('# Response:', response)
                result_text = response['choices'][0]['message']['content']
                server_flag = 1
                time.sleep(2.5)
                if server_flag:
                    break
            except Exception as e:
                server_cnt += 1
                print(e)
        return result_text
    
if __name__ == "__main__":
    summary = Summarizer()
    # summary.dialogue.append({'role': 'user', 'content': "Human: How to obtain stick?\nAI: The code for obtaining stick is as bellows:\ndef obtain_stick(inventory = {}):\n    mine({'log':2}, null); # action 1: mine 2 log without tool \n    craft({'planks':6}, {'log':2}, null); # action 2: craft 6 planks from 2 log\n    craft({'stick':2}, {'planks':1}, null); # action 3: craft 2 stick from 1 plank\n    return 'stick'\nHuman: I succeed on step 1.\nHuman: I succeed on step 2.\nHuman: I finish the task!"})
    # summary.dialogue.append({'role': 'user', 'content': "A successful plan to obtain item_frame is below and in the end my inventory has 8 planks, 1 crafting_table, 1 item_frame.\ndef obtain_item_frame(inventory = {}):\n    mine({'log':4}, null); # action 1: mine 4 log without tool\n    craft({'planks':16}, {'log':4}, null); # action 2: craft 16 planks from 4 log\n    craft({'stick':8}, {'planks':4}, null); # action 3: craft 8 stick from 4 planks first\n    mine({'leather':1}, null); # action 4: mine 1 leather without tool\n    craft({'crafting_table':1}, {'planks':4}, null); # action 5: craft 1 crafting_table from 4 planks\n    craft({'item_frame':1}, {'stick':8, 'leather':1}, 'crafting_table'); # action 6: craft 1 item_frame from 8 stick and 1 leather, on crafting_table\n    return 'item_frame'"})
    summary.dialogue.append({'role': 'user', 'content': "A successful plan to obtain wooden_pickaxe is below and in the end my inventory has 2 planks, 4 stick, 1 leather.\ndef obtain_wooden_pickaxe(inventory = {}):\n    mine({'log':2}, null); # action 1: mine 1 log without tool\n    craft({'planks':8}, {'log':2}, null); # action 2: mine 1 leather without tool\n    craft({'stick':4}, {'planks':2}, null); # action 4: craft 4 stick from 2 plank\n    mine({'log':1}, null); # action 1: mine 1 log without tool\n    craft({'planks':4}, {'log':1}, null); # action 2: mine 1 leather without tool\n    craft({'wooden_pickaxe':1, {'planks':3, 'stick':2}, crafting_table);\n    return 'wooden_pickaxe'"})

    """def obtain_stone(inventory = {}):
        mine({'log':3}, null); # action 1: mine 3 log without tool
        craft({'planks':12}, {'log':3}, null); # action 2: craft 12 planks from 3 log
        craft({'stick':4}, {'planks':2}, null); # action 3: craft 4 stick from 2 planks
        craft({'crafting_table':1}, {'planks':4}, null); # action 4: craft 1 crafting_table from 4 planks
        craft({'wooden_pickaxe':1}, {'cobblestone':3, 'stick':2}, 'crafting_table'); # action 5: craft 1 wooden_pickaxe from 3 cobblestone and 2 stick, on crafting_table
        mine({'cobblestone':3}, 'wooden_pickaxe'); # action 6: mine 3 cobblestone without tool
        return 'stone'
    """
    for i in range(100):
        print('#'*20)
        print(f'# {i+1}/100')

        response = summary.query_gpt3(summary.dialogue)
        summary.dialogue.append({'role': 'assistant', 'content': response})
        print(f'Response: {response}')

        prompt = input('User: ')
        if prompt == 'ok':
            break

        summary.dialogue.append({'role': 'user', 'content': prompt})
    pass
