import json
import os
import openai
import time

import copy

class Planner():
    def __init__(self):
        prefix = os.getcwd()
        self.openai_keys_path = os.path.join(prefix, 'data/openai_keys.txt')
        self.replan_prompt_path = os.path.join(prefix, 'data/replan_prompt2.json')

        self.openai_keys = self.load_openai_keys()
        self.replan_prompt = self.load_replan_prompt()
        
        self.dialogue = eval(self.replan_prompt)

    def load_openai_keys(self, ):
        with open(self.openai_keys_path, 'r') as f:
            context = f.read()
        return context.split('\n')

    def load_replan_prompt(self, ):
        with open(self.replan_prompt_path, 'r') as f:
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
    planner = Planner()
    planner.dialogue.append({'role': 'user', 'content': 'How to obtain a boat from scratch?'})
    for i in range(100):
        print('#'*20)
        print(f'# {i+1}/100')

        response = planner.query_gpt3(planner.dialogue)
        planner.dialogue.append({'role': 'assistant', 'content': response})
        print(f'Response: {response}')

        prompt = input('User: ')
        if prompt == 'ok':
            break

        planner.dialogue.append({'role': 'user', 'content': prompt})
    pass
