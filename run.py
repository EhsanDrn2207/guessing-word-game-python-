from chance import num_of_round
from user import get_word
from ai_word import computer_word

with open("results.txt", 'r') as file_reader:
    x = file_reader.read()
    print(x)

def intro(words):
    print("Welcome to our geme.")
    print('This is list of words that we consider for game:\n'
            f'{words}')
    print("Good Luck!")
    print("-" * 15)

def process(words):
    rounds = num_of_round(words)
    answer = computer_word(words)
    
    for i in range(rounds):
        print(f'The number rounds: {rounds - i}')   
        user = get_word(words)
        if user != answer:
            print("Your guess was wrong.")
            print("-" * 15)
            
        else:
            print("You've found the answer!")
            print("-" * 15)
            break
        
    with open('results.txt', 'a') as file_writer:
        print("The answer is {}!".format(answer))
        file_writer.write(f'{answer}\n')
        file_writer.write('----------------------\n')
        
list_of_words = ['sun', 'moon', 'tree', 'sky', 'sea', 'water', 'cloud', 'benana']

intro(list_of_words)
process(list_of_words)

