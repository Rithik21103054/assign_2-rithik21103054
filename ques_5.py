#question 5
entry=input("enter something: ")

list=entry.split()

for word in list:
    if word == "name":
       print("yes")
       break

else:
    print("no")
