1. Write a program that takes a positive integer N as input from the user and prints all natural numbers 
numbers from 1 to N, with each number followed by a space.
#Input:- N = 5 
#Output:- 1 2 3 4 5


N = int(input("Enter a positive integer: "))

i = 1

while i <= N:
    print(i)
    i += 1