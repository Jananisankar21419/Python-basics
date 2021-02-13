#python program power of given number
print("\n ===== power of num====")
def main():
     a = int(input(" enter the positive number( base):"))
     b = int(input(" enter the exponent value:"))
     count = 1
     while count <= b:
         a = b*count
         count = count + 1
         print(b)
main()
print("\n =====end of the program =====")
