from word_generator import Word_generator
from words import word_list
from hangman import Hangman

def main():
    word_generator1 = Word_generator(word_list)
    hangman = Hangman(word_generator1.get_word())
    hangman.start_game()

    while input("Play again ?  (Y/N) ").upper() == "Y":
        word_generator2 = Word_generator(word_list)
        hangman2 = Hangman(word_generator2.get_word())
        hangman2.start_game()

if __name__ == "__main__":
     main()
