# question 6
len_1=int(input("Enter length of side 1: \n"))
len_2=int(input("Enter length of side 2: \n"))
len_3=int(input("Enter length of side 3: \n"))

if len_1 + len_2 > len_3 and len_1 + len_3 > len_2 and len_3 + len_2 > len_1 :
    print("yes, triangle can be formed")

else:
    print("No, traingle cannot be formed")
    