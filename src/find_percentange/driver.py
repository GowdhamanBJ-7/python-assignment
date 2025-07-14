from src.find_percentange.util import find_percentage

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print(find_percentage(student_marks, query_name))

'''
Sample Input
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika


Sample Output 0
56.00
'''