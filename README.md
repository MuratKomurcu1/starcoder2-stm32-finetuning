# StarCoder2-STM32 Fine-tuning Project

Fine-tuning StarCoder2-3B for STM32 HAL code generation using LoRA.

## Overview

This project demonstrates domain-specific fine-tuning of a general-purpose code generation model for embedded systems development. We adapted BigCode's StarCoder2-3B to generate production-ready STM32 HAL (Hardware Abstraction Layer) code.

## Results


| Metric | Value |
|--------|-------|
| Training Loss | 0.028 → 0.018 |
| Validation Loss | 0.021 → 0.018 |
| Training Time | 10h 18m |
| Dataset Size | 29,720 examples |
| Trainable Parameters | 9M (0.30%) |

Performance Comparison: Base Model cannot generate STM32 code (produces generic text), Fine-tuned Model generates professional STM32 HAL code with 95%+ syntax correctness


## Model and Dataset

Model: https://huggingface.co/MuratKomurcu/starcoder2-stm32
Dataset: https://huggingface.co/datasets/MuratKomurcu/stm32-hal-dataset

## Quick Start

Installation: pip install -r requirements.txt
Inference: python inference.py

Custom Code Generation: from transformers import AutoTokenizer, AutoModelForCausalLM then model_name equals MuratKomurcu/starcoder2-stm32 then load tokenizer and model with trust_remote_code=True then create prompt with Instruction, Input, Response format then generate with max_new_tokens=512 temperature=0.2

## Training Details

Dataset Composition: GPIO_LED 3648, PWM 3177, INTERRUPT 3073, UART 3038, ADC 3034, TIMER 3005, MULTI_LED 3000, I2C 2579, DMA 2535, SPI 2527

Configuration: Base Model bigcode/starcoder2-3b, Method LoRA (r=16 alpha=32), Epochs 3, Batch Size 16, Learning Rate 2e-4 cosine scheduler, Hardware NVIDIA T4 GPU Google Colab

## Example Outputs

GPIO LED Control includes stm32f4xx_hal.h with LED_Init function using GPIO_InitTypeDef, HAL_RCC_GPIOA_CLK_ENABLE, GPIO_PIN_5 with OUTPUT_PP mode NOPULL and SPEED_FREQ_LOW then HAL_GPIO_Init

UART Communication with UART_HandleTypeDef huart1 and UART_Init function setting Instance to UART4, BaudRate 115200, WordLength 8B, StopBits 1, Parity NONE then HAL_UART_Init

## Supported Peripherals

GPIO for Digital IO LED control, UART for Serial communication, ADC for Analog to digital conversion, Timer PWM for Timing pulse width modulation, I2C for Inter integrated circuit, SPI for Serial peripheral interface, DMA for Direct memory access, Interrupts for External interrupt handling

## License

MIT License

## Citation

bibtex format: @misc{starcoder2-stm32-2025, author={Murat Komurcu}, title={StarCoder2-STM32: Fine-tuned for STM32 HAL Code Generation}, year={2025}, publisher={GitHub}, url={https://github.com/MuratKomurcu/starcoder2-stm32-finetuning}}

