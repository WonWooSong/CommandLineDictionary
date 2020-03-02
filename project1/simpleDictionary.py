import json

data = json.load(open("data.json"))

def dictionary(word):
    return data[word]

user_input = input("Enter a word: ")
output = dictionary(user_input)
print(output)