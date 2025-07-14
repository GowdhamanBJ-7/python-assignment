from collections import namedtuple


def named_tuple(n, columns, fields):
    Student = namedtuple('Student', columns)
    students = [Student(*line.split()) for line in fields]
    total_marks = sum(int(s.MARKS) for s in students)
    return f"{total_marks / n:.2f}"
'''
def named_tuple(n, fields):
    Student = namedtuple('student', fields)
    total_marks = 0
    for _ in range(n):
        student = Student(*input().split())
        total_marks += int(student.MARKS)
    return f"{total_marks / n:.2f}"'''

