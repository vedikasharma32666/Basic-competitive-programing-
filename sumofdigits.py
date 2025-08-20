#9. Take an integer N as input. Your task is to calculate and print the sum of the digits of the given number.
#Input:- N = 1589 
#Output:- 23 
#Explaination:- For the number 1589, the digits are 1,5,8,9. The Sum(1589) = 1+5+8+9 = 23.

N = int(input("enter a number"))
s=0
while(N>0):
    digit=N%10
    N=N//10
    s+=digit 
    
print(s)
