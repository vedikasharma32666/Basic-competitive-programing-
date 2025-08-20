#13. Write a program to input two numbers(A & B) from the user and print the maximum element among A AND B.

A=int(input("enter a number"))
B=int(input("enter a number"))
if A > B:
    print("The maximum element is:", A)
elif B > A:
    print("The maximum element is:", B)
else:
    print("Both numbers are equal.")