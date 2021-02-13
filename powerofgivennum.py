#python program for power of given number.
num = int(input(" enter any postive integer : "))
expo = int(input(" enetr the exponent value :"))
power = 1
for i in range(1,expo + 1):
    power = power * num
print(" the result of " , num," power",expo ,"=", power)   

