'''
Write a code get an integer number as input and print the sum of the digits.

Input Description:
A single line containing an integer.

Output Description:
Print the sum of the digits of the integer.

Sample Input :
124
Sample Output :
7
'''

a=int(input())
sum=0
while a>0:
    d=a%10
    sum=sum+d
    a=a//10
print(sum)