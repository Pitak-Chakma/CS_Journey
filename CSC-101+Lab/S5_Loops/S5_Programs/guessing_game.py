import random 

target = random.randint(1,10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < target:
        print("Low, Try Again.")
    elif guess > target:
        print("High, Try Again")
    else:
        print("Congratulations, You Won!!")
        restart = input("Do You want to continue? (Yes/No): ")
        if restart == "No":
            print("Take Care!!")
            break 
        else:
            target = random.randint(1,10)