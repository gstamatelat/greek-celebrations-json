import json
import re

with open('celebrations.json', encoding='utf-8') as json_file:
    json_celebrations = json.load(json_file)

for entry in json_celebrations:
    if "names" in entry["celebrations"]:
        for name in entry["celebrations"]["names"]:
            assert re.search(r'\s', name) is None
            assert re.search(r'[^Α-Ω]', name) is None
