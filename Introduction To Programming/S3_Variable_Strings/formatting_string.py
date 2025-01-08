x = 3

formatted = f"1st : I've told you {x + 1} million times already"
print(formatted) # data type conversion happened behind the scene

# works with data types other than strings 

# older method 
formatted = "2nd : I've told you {} million times already".format(x+1)
print(formatted)