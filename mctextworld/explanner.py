import json
import os
import openai
import time

import copy

class Explanner():
    def __init__(self):
        prefix = os.getcwd()
        self.openai_keys_path = os.path.join(prefix, 'data/openai_keys.txt')
        self.explain_prompt_path = os.path.join(prefix, 'data/explain_prompt.json')

        self.openai_keys = self.load_openai_keys()
        self.explain_prompt = self.load_explain_prompt()
        
        self.dialogue = eval(self.explain_prompt)

    def load_openai_keys(self, ):
        with open(self.openai_keys_path, 'r') as f:
            context = f.read()
        return context.split('\n')

    def load_explain_prompt(self, ):
        with open(self.explain_prompt_path, 'r') as f:
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
    explanner = Explanner()
    prompt = input('input your prompt: ')
    explanner.dialogue.append({'role': 'user', 'content': prompt})
    
    response = explanner.query_gpt3(explanner.dialogue)
    print(f'Response: {response}')
    pass
