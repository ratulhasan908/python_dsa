import random

print("Welcome to Number guessing Game with Ratul")
min = int(input("Enter a min range of the game "))
max = int(input("Enter the max range of the game "))

n = random.randrange(min, max)
guess = int(input("Enter your guess here "))

while n != guess:
    if(guess > n):
        print("Too high ")
        guess = int(input("Try again "))
    elif(guess < n) :
        print("Too Low")
        guess = int(input("Try once again "))
    else:
        break
print("Your answer is right, Congrats !!!")

