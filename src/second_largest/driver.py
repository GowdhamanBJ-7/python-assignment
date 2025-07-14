from src.second_largest.util import second_largest

n = int(input('Enter N number of score: '))
arr = list(map(int, input('Enter the scores: ').split()))

result = second_largest(arr)
print(result)

'''
sample input
Enter N number of score: 5
Enter the scores: 4 2 4 2 1
'''

'''
sample output :  2
'''