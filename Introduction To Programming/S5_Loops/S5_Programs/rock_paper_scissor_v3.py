import random

print("...Rocks...")
print("...Paper...")
print("...Scissors...")


computer_score = 0
player_score = 0

while (computer_score < 2) and (player_score < 2):
    # generate computer choice
    computer = random.randint(1,3)
    if computer == 1:
        computer = "rock"
    elif computer == 2:
        computer = "paper"
    else:
        computer = "scissors"

    # generate player choice
    player = input("Rock Paper or Scissors?: ").lower()

    # validate player choice
    if player != "rock" and player != "paper" and player != "scissors":
        print("Invalid input")
        

    # determine winner 
    elif player == computer:
        print("Draw")

    elif player == "rock" and computer == "scissors":
        print("Player wins")
        player_score += 1

    elif player == "scissors" and computer == "paper":
        print("Player wins")
        player_score += 1

    elif player == "paper" and computer == "rock":
        print("Player wins")
        player_score += 1
        
    else:
        print("Computer wins")
        computer_score += 1

print(f"Computer: {computer_score} Player: {player_score}")

if computer_score == 2:
    print("Computer wins :< ")
elif player_score == 2:
    print("Player wins :> ")