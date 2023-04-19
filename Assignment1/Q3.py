courses= 14
sum=0.00
for x in range (courses):
    score=input("Enter final score:")
    sum=sum+float(score)
average = sum/14
print("Total Sum=",sum)
print("Average=",average)
if (float(average)>=90):
    print("A")
elif(float(average)>=80 and float(average)<=89):
    print("B")
elif(float(average)>=75 and float(average)<=79):
    print("C")
elif(float(average)>=60 and float(average)<=69):
    print("D")
elif(float(average)<59):
    print("F")




