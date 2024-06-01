def defualt_round(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return int((number - 1) / 2)

def num_of_round(list_of_words):
    class EqualNumError(Exception):
        pass   
    
    class GreaterNumError(Exception):
        pass 

    num_of_word = len(list_of_words)
    
    while True:
        try:
            user_input = input('How many chances do you want to '
                        'have for guessing the right answer?: ')            
            if int(user_input) == num_of_word:
                raise EqualNumError
            
            elif int(user_input) > num_of_word:
                raise GreaterNumError

        except ValueError:
            print("Your input is invalid, Please try again.")
            print('-' * 20)
            
        except EqualNumError:
            print('Your chances can not be equal to numbers of the words. Please try again. ')
            print('-' * 20)
            
        except GreaterNumError:
            print('Your chance can not be more than words. '
                'Please try again.')
            print('-' * 20)

        else:                       
            if int(user_input) == 0: 
                return defualt_round(num_of_word)
            else:
                return int(user_input)
            

