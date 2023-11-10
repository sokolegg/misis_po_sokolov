from fastapi import FastAPI

import requests
import random
import os

app = FastAPI()

def openai_request(equation: str):
    command = f"Посчитай это выражение: {equation} и выведи результатов только числом"
    token = os.environ["OPENAI_TOKEN"]
    print(token)
    url = "https://api.openai.com/v1/chat/completions"
    response = requests.post(url, json={
        "model": "gpt-4",
        "messages": [{"role": "user", "content": command}]
    }, headers={"Authorization": f"Bearer {token}"})
    print(response.json())
    prompt = response.json()["choices"][0]['message']["content"]

    return prompt

def openai_request_as_code(equation: str):
    command = f"{equation} - это выражение выведи строго только питон код функции вычисления без всяких описаний!! " \
              f"я его хочу запустить потом в методе eval. Не возращай как def верни одной строкой выражение"
    token = os.environ["OPENAI_TOKEN"]
    print(token)
    url = "https://api.openai.com/v1/chat/completions"
    response = requests.post(url, json={
        "model": "gpt-4",
        "messages": [{"role": "user", "content": command}]
    }, headers={"Authorization": f"Bearer {token}"})
    print(response.json())
    prompt = response.json()["choices"][0]['message']["content"]

    result = eval(prompt) # просто вычисляет код

    return result

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/calc")
def root(equation: str):
    return openai_request(equation)

@app.post("/calc2")
def root(equation: str):
    return openai_request_as_code(equation)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
