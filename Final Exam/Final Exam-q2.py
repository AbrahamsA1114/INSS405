import random as rand
def generate_random(num):
    numbers=[]
    for i in range(num):
        numbers.append(rand.randint(1,100))
    return numbers

random_numbers=generate_random(100)
print("Random List:", random_numbers)


def sort_numbers(num):
    sorted_numbers=sorted(num)
    return(sorted_numbers)

sorted_numbers=sorted(random_numbers)
print("Sorted List:",sorted_numbers)



