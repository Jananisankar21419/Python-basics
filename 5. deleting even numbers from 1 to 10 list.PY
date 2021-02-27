print(" deleting even numbers from 1 to 10 ")
lil = list()
for i in range(1,11):
    lil.append(i)
print(" list of nums before deleting :", lil)
for i in  lil:
    if i %2 ==0:
        lil.remove(i)
    else:
         continue       
print("\n list of nums after deleting : ", lil)
print("\n end of the program by janani .s ")        
