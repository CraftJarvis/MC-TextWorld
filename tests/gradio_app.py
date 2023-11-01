import gradio as gr

def chat(message, history):
    pass  # Implement your chatbot here...
    print("messgae: ", message)
    print("history: ", history)
    return "Hello, world!"

gr.ChatInterface(fn=chat).launch()
