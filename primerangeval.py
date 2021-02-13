small = 900
high = 1000
print(" prime numbers ", small, "and", high, "are:")
for num in range(small, high+ 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
            else:
                print(num)