from transformers import AutoTokenizer

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype="auto", device_map="auto"
)

tokenizenizer = AutoTokenizer.from_pretrained(model_id)

text = input("Enter Prompt: ")
print(text)

inputs = tokenizenizer(text, return_tensor="pt", padding=True, truncation=True)
