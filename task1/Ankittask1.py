import random
password = str(random.randint(100, 999))

MAX_ATTEMPTS = 5

print("===== PASSWORD CRACKER GAME =====")
print("Crack the 3-digit password!")
print("You have 5 attempts.\n")

for attempt in range(1, MAX_ATTEMPTS + 1):

    while True:
        guess = input(f"Attempt {attempt}/{MAX_ATTEMPTS} - Enter a 3-digit guess: ")

        if guess.isdigit() and len(guess) == 3:
            break

        print("Invalid input! Please enter exactly 3 digits")

    if guess == password:
        print(f"\nCongratulations! You cracked the password!")
        print(f"Password: {password}")
        print(f"You cracked it in {attempt} attempt(s)")
        break

    print("\nIncorrect password. Hints:")

    password_used = [False] * 3
    guess_used = [False] * 3

    for i in range(3):
        if guess[i] == password[i]:
            print(f"{guess[i]} is correct and in the correct position")
            password_used[i] = True
            guess_used[i] = True
    for i in range(3):
        if guess_used[i]:
            continue

        found = False

        for j in range(3):
            if not password_used[j] and guess[i] == password[j]:
                print(f"{guess[i]} is correct but in the wrong position")
                password_used[j] = True
                guess_used[i] = True
                found = True
                break
        if not found:
            print(f"{guess[i]} is not present in the password.")

    print()

else:
    print("Game Over!")
    print(f"The correct password was: {password}")