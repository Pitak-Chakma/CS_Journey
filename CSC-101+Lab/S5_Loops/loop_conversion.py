# Loop conversion 

password = input("Enter your password: ")

for _ in range(999999):  # Using a large number as we don't know how many attempts needed
    if password == "Khul Ja Sim Sim":
        break
    print("Wrong Password")
    password = input("Enter your password: ")

print("You may come inside!!")





# for loop >> while loop
password = input("Enter your password: ")

while password != "Khul Ja Sim Sim":
    print("Wrong Password")
    password = input("Enter your password: ")

print("You may come inside!!")