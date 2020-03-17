import json
import argparse
from difflib import get_close_matches

data = json.load(open("data.json"))

def dictionary(word):
    word = word.lower()
    close_words = get_close_matches(word, data.keys(), cutoff=0.75)
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yesOrNo = input("Did you mean \"%s\" instead? Enter Y/y if yes, or N/n if no: " % get_close_matches(word, data.keys())[0])

        if yesOrNo == "Y" or yesOrNo == "y" or yesOrNo == "Yes" or yesOrNo == "yes":
            return data[get_close_matches(word, data.keys())[0]]
        elif yesOrNo == "N" or yesOrNo == "n" or yesOrNo == "No" or yesOrNo == "no": 
            return "This word does not exist in dictionary. Please check your spelling."
        else:
            return "Please input valid word."
    else:
        return "This word does not exist in dictionary. Please check your spelling."


parser = argparse.ArgumentParser()
parser.add_argument("-w", "--word", type=str, help="Finding word's dictionary meaning.")
args = parser.parse_args()    

output = dictionary(args.word)

if type(output) == list:
    for item in output:
        print("- " + item)
else:
    print("- " +output)