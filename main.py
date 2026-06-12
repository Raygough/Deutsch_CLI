from quiz import Vocabulary

'''
Promgram Driver
'''

def Main():
    print('''
        Welcome to the Detusch CLI Tool!
        Please follow the prompts to use
        the tool.\n
        Please type one of the following categories: nouns, verbs, adjectives
          ''')

    user_input = input("Enter your selection: ")
    
    vocab = Vocabulary(input=user_input)

    print(Vocabulary)

Main()