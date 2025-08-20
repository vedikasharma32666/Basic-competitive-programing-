#5. Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as input from user.
#Input:- N = 10 
#Output:- 55

N = int(input("Enter a positive integer: "))

count=0
i = 1


while i <= N:
    count += i
    i += 1

print("Sum:" ,count)
