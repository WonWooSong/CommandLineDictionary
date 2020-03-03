import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def dictionary(word):
    word = word.lower()
    close_words = get_close_matches(word, data.keys(), cutoff=0.75)
    if word in data:
        return data[word]
    elif len(close_words) > 0:
        return "Did you mean \"%s\" instead?" % close_words[0]
    else:
        return "This word does not exist in dictionary. Please check your spelling."

user_input = input("Enter a word: ")
output = dictionary(user_input)
print(output)