import random

def get_random_word():
    words = ['python', 'hangman', 'programming', 'developer', 'challenge']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           
