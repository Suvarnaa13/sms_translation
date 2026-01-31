# SMS Translation System (English ⇄ Telugu) using FLAN-T5

This project implements an SMS/Text translation system that translates
English to Telugu and Telugu to English using a transformer-based model.

## Dataset
- 20,000 English–Telugu sentence pairs
- Filtered to short SMS-style sentences
- Stored in JSON format

## Model Used
- FLAN-T5 Base (Transformer Model)

## Features
- English to Telugu translation
- Telugu to English translation
- Suitable for SMS-length text
- Works on local system
- No cloud or AWS services used

## Technologies Used
- Python
- HuggingFace Datasets
- Transformer Models (FLAN-T5)

## File Description
- SCRIPT.py : Dataset loading and preprocessing
- english_to_telugu_20k.json : Bilingual dataset
- flan_t5_base.zip : Pretrained translation model

## Execution
1. Install required libraries
2. Load dataset using SCRIPT.py
3. Use model for translation tasks

## Note
This project is intended for academic use and runs completely on a local system.
