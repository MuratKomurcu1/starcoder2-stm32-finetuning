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

### Performance Comparison

- **Base Model**: Cannot generate STM32 code (produces generic text)
- **Fine-tuned Model**: Generates professional STM32 HAL code with 95%+ syntax correctness

## Model & Dataset

- **Model**: [MuratKomurcu/starcoder2-stm32](https://huggingface.co/MuratKomurcu/starcoder2-stm32)
- **Dataset**: [MuratKomurcu/stm32-hal-dataset](https://huggingface.co/datasets/MuratKomurcu/stm32-hal-dataset)

## Quick Start

### Installation
```bash
