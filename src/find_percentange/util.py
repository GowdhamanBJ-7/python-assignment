def find_percentage(student_marks,query_name):
    for name, marks in student_marks.items():
        if name == query_name:
            output = round(sum(marks) / len(marks), 3)
    return f"{output:.2f}"
