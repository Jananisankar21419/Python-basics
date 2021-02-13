#sum of n naturalnumbers.
num = 16
if num < 0:
    print(" \n enter the positive number:")
else:
    sum = 0
    #use while loop 
    while(num > 0):
        sum += num
        num -= 1
    print(" the sum is:", sum)       