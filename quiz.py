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

    def __init__(self, input):
        self.input = input
        self.word
        self.meaning

    def load_vocab() -> dict:
        with open("vocab.json", "r") as file:
            data = json.load(file)
        return data
    
    def make_word_noun(self, data, categories) -> list[str]:
        if(self.input == "nouns"):
            rand_gen = categories[random.randrange(0, len(categories))]
            bound = len(data[self.input][rand_gen])
            word_idx = random.randrange(0, bound)

            self.word = data[self.input][rand_gen][word_idx]["word"]
            self.meaning = data[self.input][rand_gen][word_idx]["meaning"]
            return [word, meaning, rand_gen, self.input]
        
        elif(self.input == "verbs"):
            rand_gen = categories[random.randrange(0, len(categories))]
            bound = len(data[self.input][rand_gen])
            word_idx = random.randrange(0, bound)

            word = data[self.input][rand_gen][word_idx]["word"]
            meaning = data[self.input][rand_gen][word_idx]["meaning"]
            return [word, meaning, rand_gen, self.input]
        
        elif(self.input == "adjectives"):
            rand_gen = categories[random.randrange(0, len(categories))]
            bound = len(data[self.input][rand_gen])
            word_idx = random.randrange(0, bound)

            word = data[self.input][rand_gen][word_idx]["word"]
            meaning = data[self.input][rand_gen][word_idx]["meaning"]
            return [word, meaning, rand_gen, self.input]
        

# class User_Quiz(Vocabulary):
#     def print_word(Rand_Word):
#         print(f"QUESTION: What does \"{word}\" mean?")

#     user_input = input("ANSWER: ")


#     if(user_input == Vocabulary.meaning):
#         print(f"RICHTIG! \"{word}\" means \"{meaning}\"")
#     else:
#         print(f"FALSCH! \"{word}\" means \"{meaning}\"")


