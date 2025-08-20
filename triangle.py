#12. You are given 3 integer angles(in degrees), A, B, and C, of a triangle. You have to tell whether the triangle is valid or not.if the su, of its angle equals 180.

a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if(a+b+c==180):
    print("the triangle is valid")
else:
    print("the triangle is not valid")