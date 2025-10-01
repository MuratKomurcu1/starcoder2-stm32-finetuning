from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = 'YOUR_USERNAME/starcoder2-stm32'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
