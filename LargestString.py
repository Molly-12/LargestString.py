str=input("Enter any String :")
L = str.split()
max=0
b=""
for i in L:
 if len(i) > max:
 b=i
 max=len(i)
print("Longest word is ",b)
