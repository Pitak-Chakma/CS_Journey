x = 0

for odd in range(11,21,2):
    x += odd

print(x)

# another way 

x = 0 

for num in range(10,21):
    if num % 2 == 1:
        x += num
 
print(x)