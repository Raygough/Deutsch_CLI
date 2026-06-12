'''
Logic for CLI Quiz Tool
'''
import json
import random



class Vocabulary():
    '''
    Creates Vocab word + meaning from JSON
    '''

    categories = ["masc", "fem", "neut"]

    def __init__(self, input, word, meaning):
        self.input = input
        self.word = word
        self.meaning = meaning

    def load_vocab() -> dict:
        with open("vocab.json", "r") as file:
            data = json.load(file)
        return data
    
    def make_word_noun(self, data, categories) -> list[str]:
        if(input == "nouns"):
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


