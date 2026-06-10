'''
Logic for CLI Quiz Tool
'''
import json
import random


'''
Creates Vocab word + meaning from JSON
'''
class Vocabulary():
    categories = ["masc", "fem", "neut"]

    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def load_vocab() -> dict:
        with open("vocab.json", "r") as file:
            data = json.load(file)
        return data
    
    def make_word(data) -> list[str]:
        


    


class Rand_Word():
    

    def make_rand_word(user_input, data):
        
        if(user_input == "nouns"):
            rand_cat = categories[random.randrange(0, len(categories))]
            bound = len(data["nouns"][rand_cat])
            rand = random.randrange(0, bound)

            word = data["nouns"][rand_cat][rand]["word"]
            meaning = data["nouns"][rand_cat][rand]["meaning"]
            return [word, meaning, rand_cat, user_input]
        
        elif(user_input == "verbs"):
            rand_cat = categories[random.randrange(0, len(categories))]
            bound = len(data["verbs"][rand_cat])
            rand = random.randrange(0, bound)

            word = data["verbs"][rand_cat][rand]["word"]
            meaning = data["verbs"][rand_cat][rand]["meaning"]
            return [word, meaning]
        
        elif(user_input == "adjectives"):
            rand_cat = categories[random.randrange(0, len(categories))]
            bound = len(data["adjectives"][rand_cat])
            rand = random.randrange(0, bound)

            word = data["adjectives"][rand_cat][rand]["word"]
            meaning = data["adjectives"][rand_cat][rand]["meaning"]
            return [word, meaning]


class User_Quiz():
    def print_word(Rand_Word):
        print(f"QUESTION: What does \"{word}\" mean?")



user_input = input("ANSWER: ")


if(user_input == meaning):
    print(f"RICHTIG! \"{word}\" means \"{meaning}\"")
else:
    print(f"FALSCH! \"{word}\" means \"{meaning}\"")


