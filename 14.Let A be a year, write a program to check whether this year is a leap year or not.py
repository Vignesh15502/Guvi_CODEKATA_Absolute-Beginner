'''
Let "A" be a year, write a program to check whether this year is a leap year or not.

Print "Y" if its a leap year and "N" if its a common year.

Input Description:
A Year is the input in the form of a positive integer.

Output Description:
Print "Y" if its a leap year and "N" if its a common year.

Sample Input :
2020
Sample Output :
Y
'''

a=int(input())
if a%100==0:
    if a%400==0:
        print("y")
    else:
        print("N")
else:
    if a%4==0:
        print("Y")
    else:
        print("N")