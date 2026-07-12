from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

model = AutoModelForCausalLM.from_pretrained(model_id)

tokenizer = AutoTokenizer.from_pretrained(model_id)

text = input("Enter Prompt: ")
print(text)
encoded = tokenizer.encode(text)
print(encoded)
print(tokenizer.decode(encoded))
print(tokenizer.tokenize(text))
# inputs = tokenizer(text, return_tensor="pt", padding=True, truncation=True)
