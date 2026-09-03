import random

words = ["python", "machine", "learning", "data", "science"]

secret_word = random.choice(words)

guessed_word = ["_"] * len(secret_word)
chances = 6

while chances > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Chances left:", chances)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess and guessed_word[i] == "_":
                guessed_word[i] = guess
                break

        print("Correct!")
    else:
        chances -= 1
        print("Wrong guess! Chances left:", chances)

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\nGame Over!")
    print("The secret word was:", secret_word)
   # '_', '_','_'
   #_ _ _
