import numpy as np
from src.Floor_Ceil_and_Rint.util import floor_Ceil_Rint

input_array = np.array(list(map(float, input().split())))

print(floor_Ceil_Rint(input_array))


'''
Sample Input
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

Sample Output

[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
'''