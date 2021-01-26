#program for swapping two variables using tuple assignment
no1 = int(input("Enter the first number:"))
no2 = int(input("enter the second number:"))

print("value of no1 before swapping :",no1)
print(" value of no2 after swapping :",no2)

#swapping two values
no1 , no2 = no2 , no1

#after swapping 
print("value of no1 after swapping:",no1)
print("value of no2 after swapping:",no2)