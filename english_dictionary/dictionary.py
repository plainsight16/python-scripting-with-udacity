import json
from difflib import get_close_matches


dictionary = json.load(open("./data.json", "r"))

user_input = input("Enter query word: ")


def translate(word):
    word = word.lower()
    if word in dictionary:
        answers = dictionary[word]
        return answers

    elif len(get_close_matches(word, dictionary.keys())) > 0:
        similar_word = get_close_matches(word, dictionary.keys())[0]

        question = input(
            "Did you mean {} instead?\nEnter Y/N: ".format(similar_word))

        return response(question, similar_word)
    else:
        return "Word does not exist. Please double check"


def response(answer, similar_word):
    answer = answer.upper()
    if answer == "Y":
        return(translate(similar_word))
    elif answer == "N":
        return "Word does not exist. Please double check"
    else:
        answer = input(
            "We did not get your entry. Please try again\nEnter Y/N: ")
        return response(answer, similar_word)


output = translate(user_input)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
