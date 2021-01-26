#program for circlAting n values
print(" \n circulating the n variables")
list_of_vals= [ 1,2,3,4,5]
print("list :",list_of_vals)
n= int(input("\n  enter the no of times:"))
circulate = list_of_vals[n :] + list_of_vals[:n]
print(" \n calculated values : ", circulate)
#end of the program