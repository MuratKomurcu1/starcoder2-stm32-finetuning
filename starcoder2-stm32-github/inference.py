from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = 'MuratKomurcu/starcoder2-stm32'
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, torch_dtype=torch.float16, device_map='auto')

def generate_stm32_code(instruction, input_text, max_length=512):
    prompt = f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:
{input_text}

### Response:
"""
    inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=max_length, temperature=0.2, top_p=0.95, do_sample=True, pad_token_id=tokenizer.eos_token_id)
    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = generated.split('### Response:')[-1].strip()
    return response

if __name__ == '__main__':
    print('STM32 Code Generator Ready')
    print('Example 1: GPIO LED')
    code1 = generate_stm32_code('Create GPIO LED control', 'Write STM32 HAL code for LED on GPIOA PIN 5')
    print(code1)
    print('\nExample 2: UART')
    code2 = generate_stm32_code('Implement UART communication', 'Write STM32 HAL code for UART at 115200 baud')
    print(code2)
