#12. You are given two integers A and B. You have to find the value of A^B. 
#Input:- A = 2 , B = 3 
#Output:- 8 
#Explaination:- For A=2 and B=3, the value of 2^3 = 2 * 2 * 2 = 8.

'''A = int(input("Enter a number "))
B = int(input("Enter a number "))

count=1

i = 1

while i <= B:
    count = count * A
    i = i + 1

print("count:", count)'''
