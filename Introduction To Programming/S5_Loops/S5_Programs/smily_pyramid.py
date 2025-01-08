print("---- For Loop ----")

for i in range(1,10):
    print("\U0001f600" * i)

print("---- While Loop ----")
num = 1
while num<10:
    print("\U0001f600" * num)
    num += 1

print("---- Both Loop ----")

num = 1
for i in range(1,10): 
    while num<i+1:
        print("\U0001f600" * num)
        num = num + 1
