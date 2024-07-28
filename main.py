import random

n = random.randint(1,100)
a = -1
guesses = 1

while(a != n):
    a = int(input("Guess any number : "))

    if(a > n):
        print("Guess lower")
        guesses += 1

    elif(a < n):
        print("Guess higher")
        guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempts")