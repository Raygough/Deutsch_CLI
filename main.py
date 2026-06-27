import argparse, time
from quiz import Word, Quiz, Session
from quiz import valid_rounds


'''
Promgram Driver
'''

def time_cal(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        user_func = func(*args, **kwargs)
        end = time.time()

        print(f"your total session time " \
              f"was {end - start:.2f} seconds")
        return user_func

    return wrapper

@time_cal
def Main():
    print('''
        Welcome to the Detusch CLI Tool!\n
        Please follow the prompts to use the tool.\n
        Please type one of the following categories: nouns, verbs, adjectives
          ''')

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--category", type=str, help="category of word",
                        choices=["nouns", "verbs", "adjectives"], required=True)
    
    parser.add_argument("-r", "--rounds", type=valid_rounds, help="number of questions", required=True)
    args = parser.parse_args()

    user_cat = args.category
    user_rounds = args.rounds
    
    quiz = Quiz()
    print("You can press \"x\" at any point to exit the session\n")

    for i in range(user_rounds):
        word = Word(input=user_cat)
        word.make_word()
        if not quiz.test(word.word, word.meaning):
            break
    
    rounds_done = user_rounds if user_rounds == quiz.num_rounds else quiz.num_rounds
    session = Session(rounds_done, quiz.correct)
    session.summary()

Main()