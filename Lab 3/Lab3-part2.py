score1 = input("Enter score for INSS405:")
score2 = input("Enter score for BUIS360:")
score3 = input("Enter score for DANL470:")

sum = int(score1)+int(score2)+int(score3)
print("Sum=",sum)

average = sum/3
print("Average=", average)

if (float(average)>90):
    print("A")
if (float(average)>=70 and float(average) <=89):
    print("B")
if (float(average)>=60 and float(average)<=69):
    print("C")
if (float(average)<59):
    print("F")


