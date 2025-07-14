from util import noIdea

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = noIdea(arr,A,B)
print(result)

'''
sample input 
3 2
1 5 3
3 1
5 7
'''

'''
sample output
1
'''