import json

with open("real_data/real_transcriptions.json", "r", encoding="utf-8") as file:
    data = json.load(file)

samples_with_errors = 0
for sample in data:
    error = False
    for word in sample["words"]:
        if word["mispronunciations"]: error = True
    if error: samples_with_errors += 1
print(samples_with_errors)