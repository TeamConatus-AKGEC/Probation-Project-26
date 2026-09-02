import random

def play_secret_word():
    words = ["python", "machine", "learning", "data", "science"]
    secret_word = random.choice(words)
    
    guessed_letters = []
    chances = 6

    while chances > 0:

        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        
        print("\nWord:", display)

        if "_" not in display:
            print("Congratulations-__- You guessed the word:", secret_word)
            break
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct")
        else:
            chances -= 1
            print("Wrong guess! Chances left:", chances)

    if chances == 0:
        print("\nGame Over! The word was:", secret_word)

play_secret_word()
