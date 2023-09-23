#voting program
age=int(input("enter your age"))
citizenship=input("enter your citizenship")

if age >=18 and citizenship in ["kenya", "tanzania", "uganda"]:
    print("you're eligible to vote")
else:
    print("you're not eligible to vote")
