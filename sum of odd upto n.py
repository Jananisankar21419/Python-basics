#sum of odd upto to n
n = int(input(" enter any odd number :")
sum= 0
for i in range(1,n+1):
       if(not(i % 2) == 0):
         sum += i;  
print("\n sum of odd numbers",n)       
