import pandas as pd

payloads_file = "combined_payloads.txt"
valid_queries_file = "valid_queries.txt"
output_file = "dataset.csv"

with open(payloads_file, "r", encoding="utf-8") as f:
    payloads = f.readlines()

with open(valid_queries_file, "r", encoding="utf-8") as f:
    valid_queries = f.readlines()

payloads = [line.strip() for line in payloads if line.strip()]
valid_queries = [line.strip() for line in valid_queries if line.strip()]

data = []
for sentence in payloads:
    data.append({"Sentence": sentence, "Label": 1})

for sentence in valid_queries:
    data.append({"Sentence": sentence, "Label": 0})

df = pd.DataFrame(data)

df.to_csv(output_file, index=False)

print(f"Dataset saved to {output_file}")
