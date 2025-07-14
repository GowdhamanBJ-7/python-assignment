from src.named_tuple.util import named_tuple

n = int(input())
columns = input().split()
fields = [input() for _ in range(n)]

result = named_tuple(n, columns, fields)
print(result)

'''
sample input
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
'''

'''
sample output
average = (97+50+91+72+80)/5 

78.00
'''