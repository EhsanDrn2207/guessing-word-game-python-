import random

def random_list():
    list_of_words1 = ["apple", "orange", "banana", "melon", "date", "peach", "pear", "lemon"]
    list_of_words2 = ["water", "sea", "rain", "snow", "cloud", "sky", "sun", "moon", "star", 'nigth']
    list_of_words3 = ["tree", "stone", "wood", "gold", "silver", "iron", "wind", "butterfly"]
    list_of_words4 = ["table", "pen", "pencil", "eraser", "book", "notebook", "paper", "bag"]
    list_of_words5 = ["Ehsan", "Parham", "Amin", "Daniyal", "Iliya", "Arshiya", "Diayana", "Shamim"]
    my_lists = [list_of_words1, list_of_words2, list_of_words3, list_of_words4, list_of_words5]
    my_list_of_words = random.choice(my_lists)
    return my_list_of_words

