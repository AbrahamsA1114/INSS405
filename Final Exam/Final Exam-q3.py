import random as rand

def generate_random(num):
    numbers=[]
    for i in range(num):
        numbers.append(rand.randint(1,100))
    return numbers

random_numbers=generate_random(100)
for num in random_numbers:
    if num % 2 != 0:
        print(num)