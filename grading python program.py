#grading system
english=int(input("Enter the english marks: "))

kiswahili=int(input("Enter the kiswahili marks: "))

maths=int(input("Enter the maths marks: "))

science=int(input("Enter the science marks: "))

total=(english + kiswahili + maths + science)

average = total/4

print(("total marks = ",) total)
print(("average marks= ",) average)

if average >=70 and average <= 100 :
    print("grade = A")
    
if average >=60 and average <=69 :
    print("grade = B")

if average >=50 and average <=59 :
    print("grade = C")

if average >=40 and average <=49 :
    print("grade = D")

if average >=30 and average <=39 :
    print("grade = E")

if average <30 :
    print("grade = Fail")

