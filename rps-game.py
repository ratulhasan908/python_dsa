import random

player = input("Select Rock, Paper or Scissor : ").lower()
computer = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("Computer has selected ", computer)

if player == "Rock" and computer == "Paper":
    print("Computer Won")
elif player == "paper" and computer =="scissor":
    print("Computer Won")
elif player == 'scissor' and computer == 'rock':
    print("Computer won")
elif player == computer:
    print("Tie")
else:
    print("You won bro, Congrats !!")