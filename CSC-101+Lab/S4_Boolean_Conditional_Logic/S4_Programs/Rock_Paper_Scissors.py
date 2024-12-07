print("...Rocks...")
print("...Paper...")
print("...Scissors...")

player1 = input("Player 1: ")
print("No Cheating")
print("No Cheating")
print("No Cheating")
print("No Cheating")
print("No Cheating")
print("No Cheating")
print("No Cheating")
print("No Cheating")
player2 = input("Player 2: ")

print("-----SHOOT-----")

if (player1 and player2):
    if player1 == player2:
        print("Draw")
    elif player1 == "Rock" and player2 == "Scissors":
        print("Player 1 wins")
    elif player1 == "Scissors" and player2 == "Paper":
        print("Player 1 wins")
    elif player1 == "Paper" and player2 == "Rock":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
else:
    print("Give your input properly")