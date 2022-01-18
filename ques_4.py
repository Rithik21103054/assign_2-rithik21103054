#question 4
num_1=float(input("enter first number: \n"))
num_2=float(input("enter second number: \n"))
num_3=float(input("enter third number: \n"))

if (num_1>num_2) and (num_1>num_3) :
    largest_number= num_1
elif (num_2>num_1) and (num_2>num_3 ):
    largest_number= num_2
else:
    largest_number= num_3

print("the largest number is : " ,(largest_number) )

