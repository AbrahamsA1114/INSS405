sum=0.00
for x in range(4):
    score= input("Enter final score:")
    sum=sum+float(score)
average=sum/4
print("Total Sum=",sum)
print("Average=",average)
if float(average)>=90:
    print("A")
elif float(average)>=80 and float(average)<=89:
    print("B")
elif float(average)>=70 and float(average)<=79:
    print("C")
elif float(average)>=60 and float(average)<=69:
    print("D")
elif float(average)>=50 and float(average)<=59:
    print("E")
else:
    print("F")
