import random

print("...Rocks...")
print("...Paper...")
print("...Scissors...") 

# 1 - rocks 
# 2 - paper
# 3 - scissors

player1 = random.randint(1,3)
player2 = int(input("Player 2: "))

print("-----SHOOT-----")    

if player2:
    if player1 == player2:
        print("Draw")
    elif player1 == 1 and player2 == 3:
        print("Player 1 wins")
    elif player1 == 2 and player2 == 1:
        print("Player 1 wins")
    elif player1 == 3 and player2 == 2:
        print("Player 1 wins")
    else:
        print("Player 2 wins")
else:
    print("Give your input properly")