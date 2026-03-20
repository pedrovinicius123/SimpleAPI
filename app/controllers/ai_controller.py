from ollama import Client

client = Client("http://localhost:11434")

def chat(query:str):
    response = client.chat(query, stream=True)
    return response
