#5.take an integer A as input. you have to tell whether A is divible by both 5 and 11 or not.

A=int(input("enter a number"))
if(A%5==0) and (A%11==0):
   print("A is divisible by both 5 and 11")
else:
   print("A is not divisible by both 5 and 11")