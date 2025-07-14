from src.linear_algebra.util import linearAlgebra

# Read matrix size
n = int(input())

# Read n rows into a list of lists
matrix = [list(map(float, input().split())) for _ in range(n)]

print(linearAlgebra(matrix))

'''
Sample Input

2
1.1 1.1
1.1 1.1

Sample Output

0.0
'''