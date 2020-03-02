import json

data = json.load(open("data.json"))

def dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "This word does not exist in dictionary. Please check your spelling."

user_input = input("Enter a word: ")
output = dictionary(user_input)
print(output)