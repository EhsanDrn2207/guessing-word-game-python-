def get_word(words):
    class InvalidWordError(Exception):
        pass
    
    while True:
        try:
            user_input = input("Please enter a word: ")
            if user_input.isdigit():
                raise ValueError
            
            if user_input not in words:
                raise InvalidWordError()
                        
        except InvalidWordError:
            print("Your input is not in the list. please try again.")
            print("-" * 15)
        except ValueError:
            print("You have not enter number. Please try again.")
            print("-" * 15)

        else:
            return user_input