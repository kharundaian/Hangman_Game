import random

class Word_generator:
    def __init__(self, words):
        self.words = words

    def get_word(self):
        word = random.choice(self.words)
        return word.upper()