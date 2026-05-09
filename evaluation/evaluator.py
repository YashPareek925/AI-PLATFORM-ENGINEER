import json
import time
import requests


with open("evaluation/prompts.json", "r") as file:
    prompts = json.load(file)


results = []


for prompt in prompts:
    start_time = time.time()

    try:
        response = requests.post("http://127.0.0.1:8000/generate",
                json={"prompt": prompt}, timeout=10)
    
    except requests.exceptions.ConnectionError:
        print("Server nahi chal raha — pehle uvicorn start karo")

    end_time = time.time()

    latency = end_time - start_time

    results.append({
        "prompt": prompt,
        "status_code": response.status_code,
        "latency": latency
    })


print(results)
