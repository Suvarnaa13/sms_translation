from datasets import load_dataset
import json

# Load dataset
ds = load_dataset("MRR24/English_to_Telugu_Bilingual_Sentence_Pairs")

# Lists for both directions
en_te_pairs = []
te_en_pairs = []

for example in ds["train"]:
    en = example["Input"]
    te = example["Output"]

    # Filter short SMS-style pairs
    if len(en.split()) <= 20 and len(te.split()) <= 20:
        # English → Telugu
        if len(en_te_pairs) < 20000:
            en_te_pairs.append({"English": en, "Telugu": te})

        # Telugu → English
        if len(te_en_pairs) < 20000:
            te_en_pairs.append({"Telugu": te, "English": en})

    # Stop once both lists reach 20k
    if len(en_te_pairs) == 20000 and len(te_en_pairs) == 20000:
        break

print(f"Collected {len(en_te_pairs)} English→Telugu pairs")
print(f"Collected {len(te_en_pairs)} Telugu→English pairs")