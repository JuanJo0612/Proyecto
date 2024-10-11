import random

x = random.randint(3, 10)

if x % 3 == 1:
    x = x - 1  
else:
    x = x  + 3  


print(x)
