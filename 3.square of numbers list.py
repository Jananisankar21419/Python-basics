print("==============  start of the program ===============")
sq = []
num = [ 1,2,3,4,5,6,7,8,9,10]
def square(sq):
    for i in range(0,len(num)):
        sq.append(num[i]**2)
    return sq
print("\n user list :", num)
print("\n square of numbers",square(sq))
print(" ================end of the program=================")    