def request():
    num1 = input("Enter variable num1=")
    num2 = input("Enter variable num2=")
    num3 = input("Enter variable num3=")
    print("Sum=", addition(num1,num2,num3))
    print("Average=", average(num1,num2,num3))
    print("Maximum=",maximum(num1,num2,num3))
    print("Minimum=",minimum(num1,num2,num3))
    print("Product=",product(num1,num2,num3))
def addition(num1,num2,num3):
    sum=int(num1)+int(num2)+int(num3)
    return sum

def average(num1,num2,num3):
    sum = int(num1) + int(num2) + int(num3)
    mean=sum/3
    return mean

def maximum(num1,num2,num3):
    return max(num1,num2,num3)

def minimum(num1,num2,num3):
    return min(num1,num2,num3)

def product(num1,num2,num3):
    multiply = int(num1) * int(num2) * int(num3)
    return multiply

request()