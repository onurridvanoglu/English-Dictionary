import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def definition(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word does not exists. Please double check it."
        else:
            return "We did not understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = definition(word)

if isinstance(output, list):
    for item in output:
        print(item)
else: 
    print(output)