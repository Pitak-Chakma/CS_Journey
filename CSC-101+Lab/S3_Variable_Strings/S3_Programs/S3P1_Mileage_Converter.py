print("How Many kilometers did you cycle today?")
kms = input()

miles1 = str(float(kms)/1.60934) # string conversion for printing 
print("You cycled " + miles1 + " miles!!")

# but directly converting miles to string is not a good idea, because I might need the numeric miles later

miles2 = float(kms)/1.60934
print(f"You cycled {miles2} miles!!")

# but too many decimal points !!!! 
# can use round(target,decimal place limit)
print(f"You cycled {round(miles2,3)} miles!!")
