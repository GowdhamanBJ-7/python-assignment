from src.min_max.util import min_max
import numpy as np
n, m = map(int, input().split())
arr = np.array([list(map(int, input().split()) ) for _ in range(n) ])

print(min_max(arr))

'''
Sample Input

row - 4  col - 2

2 5
3 7
1 3
4 0

Sample Output

3
'''

'''
explanation

min axis 1 = [2,3,1,0]
max of [2,3,1,0] is 3
'''