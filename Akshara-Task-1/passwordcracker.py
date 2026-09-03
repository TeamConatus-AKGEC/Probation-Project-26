
import random

password = random.randint(100, 999)
attempt = 1

while attempt <= 5:

    guess = int(input("Enter a 3-digit number: "))

    if guess < 100 or guess > 999:
        print("Invalid input! Enter only a 3-digit number.")
        continue

    if guess == password:
        print("Congratulations! You cracked the password.")
        print("Attempts taken:", attempt)
        break

    p1 = password // 100
    p2 = (password // 10) % 10
    p3 = password % 10

    g1 = guess // 100
    g2 = (guess // 10) % 10
    g3 = guess % 10

    print("Hints:")

    if g1 == p1:
        print(g1, "Correct position")
    elif g1 == p2 or g1 == p3:
        print(g1, "Wrong position")
    else:
        print(g1, "Not present")

    if g2 == p2:
        print(g2, "Correct position")
    elif g2 == p1 or g2 == p3:
        print(g2, "Wrong position")
    else:
        print(g2, "Not present")

    if g3 == p3:
        print(g3, "Correct position")
    elif g3 == p1 or g3 == p2:
        print(g3, "Wrong position")
    else:
        print(g3, "Not present")

    attempt += 1

if attempt > 5:
    print("Game Over!")
    print("Correct password was:", password)