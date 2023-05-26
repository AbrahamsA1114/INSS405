def input_numbers(get_numbers):
    numbers=[]
    for i in range(get_numbers):
        num=int(input("Enter a number:"))
        numbers.append(num)
    return numbers

numbers_list=input_numbers(10)
print("Numbers Entered:",numbers_list)

def calculate_sum(numbers):
    sum=0.00
    for i in range(10):
        sum=sum+numbers[i]
    return sum

sum=calculate_sum(numbers_list)
print("List Sum:",sum)
def calculate_mean(numbers):
    average=sum/len(numbers)
    return average

mean=calculate_mean(numbers_list)
print("List Average:",mean)

def calculate_median(numbers):
    import statistics
    mid = statistics.median(numbers)
    return mid

median=calculate_median(numbers_list)
print("List Median:", median)


