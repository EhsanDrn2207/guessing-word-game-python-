import random

def random_list():
    list_of_words1 = ["apple","orange", "banana", "melon", "date", "peach", "pear", "lemon"]
    list_of_words2 = ["water", "sea", "rain", "snow", "cloud", "sky", "sun", "moon", "star", 'nigth']
    list_of_words3 = ["tree", "stone", "wood", "gold", "silver", "iron", "wind", "butterfly"]
    list_of_words4 = ["table", "pen", "pencil", "eraser", "book", "notebook", "paper", "bag"]
    list_of_words5 = ["Ehsan", "Parham", "Amin", "Daniyal", "Iliya", "Arshiya", "Mehdi"]
    list_of_words6 = ["lion", "tiger", "bear", "wolf", "eagle", "elephant", "snake", "whale"]
    list_of_words7 = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "black"]
    list_of_words8 = ["guitar", "piano", "violin", "drums", "flute", "trumpet", "saxophone", "cello"]
    list_of_words9 = ["car", "train", "bicycle", "bus", "airplane", "boat", "motorcycle", "subway"]
    list_of_words10 = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    my_lists = [
    list_of_words1,
     list_of_words2,
     list_of_words3,
     list_of_words4,
     list_of_words5,
     list_of_words6,
     list_of_words7,
     list_of_words8,
     list_of_words9,
     list_of_words10,
     ]
    
    my_list_of_words = random.choice(my_lists)
    return my_list_of_words

