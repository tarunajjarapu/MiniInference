from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

import scheduler

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

model = AutoModelForCausalLM.from_pretrained(model_id)

tokenizer = AutoTokenizer.from_pretrained(model_id)

text = input("Enter Prompt: ")
print(text)
encoded = tokenizer.encode(text)
print(encoded)
print(tokenizer.decode(encoded))
print(tokenizer.tokenize(text))

for name, param in model.named_parameters():
    print(name)
    print(param.shape)
    print(param.dtype)
    print(param.device)

user = input("User Name: ")
next_request = input("Next Prompt or q to quit: ")
all_requests = []
while next_request != "q":
    all_requests.append(next_request)
    next_request = input("Next Prompt or q to quit")

state = scheduler.Router
scheduled_tasks = []
router = scheduler.Router
for request in all_requests:
    scheduled_tasks.append(scheduler.Request(user, tokenizer.tokenize(request)))

for task in scheduled_tasks:
    router.schedule(task)

# inputs = tokenizer(text, return_tensor="pt", padding=True, truncation=True)
