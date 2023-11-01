# import gradio as gr
# from mctextworld.simulator import *

# title = "Minecraft TextWorld"
# description = "Welcome to a text-based world that simulates the rules of Minecraft. In this interactive environment, you can select actions to engage with the virtual world and accomplish various tasks."

# def chat(message, history):
#     # Implement your chatbot here...
#     return "Hello, world!"

# gr.ChatInterface(
#   fn=chat,
#   title = title,
#   description = description,
#   theme="gradio/base",
#   ).launch()



# def get_response(message, history):
#     pass


import gradio as gr
import random
import time

with gr.Blocks(theme = "gradio/base") as demo:
    chatbot = gr.Chatbot(value=[[None, "Hello, how are you?"]])
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history.append((message, bot_message))
        # time.sleep(2)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()




# def chat(message, history):
#     pass  # Implement your chatbot here...
#     print("messgae: ", message) # hahahah
#     print("history: ", history) # [['hello', 'Hello, world!'], ['hello', 'Hello, world!']]
#     return "Hello, world!"

# gr.ChatInterface(fn=chat).launch()


# def repeater(message):
#     return message

# iface = gr.Interface(fn=repeater, inputs="text", outputs="text")
# iface.launch()

