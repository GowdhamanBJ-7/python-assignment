from src.iterables.utils import iterables

# Input
n = int(input())
letters = input().split()
k = int(input())

result = iterables(letters,k)
print(result)

'''
Sample Input

4 
a a c d
2

Sample Output
0.8333
'''