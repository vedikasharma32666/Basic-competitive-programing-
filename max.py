 #.6 read three integers and print their maximum.
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if(a>b and a>c):
   print("a is maximum")
elif(b>c and b>a):
   print("b is maximum")
else:
   print("c is maximum")