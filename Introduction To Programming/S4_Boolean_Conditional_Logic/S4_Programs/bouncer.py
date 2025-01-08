# asks for age 
# 18 - 21 wristband 
# 21+  - can drink + normal entry 
# else no entry

age = input("What is your age?: ")

if age:
    age = int(age)

    if age >21:
        print("You can enter and drink")
    elif age >= 18:
        print("You can enter but need wristband")
    else:
        print("You cannot enter")
else:
     print("Enter a Value")