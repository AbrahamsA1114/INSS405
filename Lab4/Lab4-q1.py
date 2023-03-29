import random as rand
sum=0.00
for i in range (1000):
    print("i=", i)
    sum=sum+rand.randint(1,1000)
print("Final Sum=",sum)
average=sum/1000
print("Final Average=",average)

