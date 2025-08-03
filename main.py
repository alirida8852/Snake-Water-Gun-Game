import random
Your_score=0
computer_score=0
youdict={1: "snake", -1: "water", 0: "gun"}
for i in range(1,4):
    computer = random.choice([0, 1, -1])
    you= int(input("Enter 1 for snake, -1 for water, 0 for gun: "))
    your_choice = youdict[you]
    computer_choice =youdict[computer]
    if computer == you:
     print(f"Round {i} \nIt's a tie! \nYou both chose {your_choice}.")
    elif (computer == 0 and you == -1) or (computer == -1 and you == 1) or (computer == 1 and you == 0):
     Your_score += 1
     print(f"Round {i} \nYou win! \n{your_choice} beats {computer_choice}.")
    else:
     computer_score += 1
     print(f"Round {i} \nYou lose! \n{computer_choice} beats {your_choice}.")

print(f"Your score: {Your_score}, Computer's score: {computer_score}")
if Your_score > computer_score:
    print("Congratulations! You win the game!🎉")
elif Your_score < computer_score:
    print("Sorry, you lose. Better luck next time!🥲")
else:
    print("It's a draw! 🤝")
    