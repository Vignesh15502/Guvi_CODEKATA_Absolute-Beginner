'''
Write a code to get an integer N and print the sum of  values from 1 to N.

Input Description:
A single line contains an integer N.

Output Description:
Print the sum of values from 1 to N.

Sample Input :
10
Sample Output :
55
'''

N=input()
arr=[]
for i in range(1,int(N)+1):
    arr.append(i)
print(sum(arr))
    
    