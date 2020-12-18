class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed = False
        self.guessed_letters = []
        self.guessed_words = []
        self.tries = 6
        self.word_completion = "_" * len(word)


    def greating(self):
        print("Let's play Hangman!")
        print(self.display_hangman())
        print(self.word_completion)
        print("\n")

    def start_game(self):
        self.greating()
        self.check_results()

    def check_results(self):
        while not self.guessed and self.tries > 0:
            guess = input("Please guess a letter or a word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in self.guessed_letters:
                    print("You already guessed the letter", guess)
                elif guess not in self.word:
                    print(guess, "is not in the word")
                    self.tries -= 1
                    self.guessed_letters.append(guess)
                else:
                    print("Good job", guess, "is in the word!")
                    self.guessed_letters.append(guess)
                    word_as_list = list(self.word_completion)
                    indices = [i for i, letter in enumerate(self.word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        self.guessed = True
            elif len(guess) == len(self.word) and guess.isalpha():
                if guess in self.guessed_words:
                    print("You already guessed the word", guess)
                elif guess != self.word:
                    print(guess, "is not the word.")
                    self.tries -= 1
                else:
                    self.guessed = True
                    self.word_completion = self.word
            else:
                print("Not a valid guess!")
            print(self.display_hangman())
            print(self.word_completion)
            print("\n")
        if self.guessed:
            print("Congrats, you guessed the word! You win!")
        else:
            print("Sorry you ran out of the tries. The word was " + self.word + " Try again")

    def display_hangman(self):
        stages = ["""
                    --------
                    |       | 
                    |       O
                    |      \\|/
                    |       |
                    |      / \\
                    -
                  """,
                  """
                      --------
                      |       |
                      |       O
                      |      \\|/
                      |       |
                      |      / 
                      -
                  """,
                  """
                      --------
                      |       |
                      |       O
                      |      \\|/
                      |       |
                      |      
                      -
                  """,
                  """
                      --------
                      |       |
                      |       O
                      |      \\|
                      |       |
                      |      
                      -
                  """,
                  """
                      --------
                      |       |
                      |       O
                      |       |
                      |       |
                      |      
                      -
                  """,
                  """
                      --------
                      |       |
                      |       O
                      |     
                      |       
                      |      
                      -
                  """,
                  """
                      --------
                      |       |
                      |       
                      |     
                      |       
                      |      
                      -


                  """,
                  ]
        return stages[self.tries]