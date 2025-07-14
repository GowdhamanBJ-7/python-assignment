from src.list.util import process_commands

N = int(input())
commands = [input() for _ in range(N)]
output = process_commands(N, commands)
for line in output:
        print(line)

'''
sample input
12
insert 0 5
insert 1 10
insert 0 6
print
remove 10
append 9
append 1
sort
print
pop
reverse
print

sample output
[6, 5, 10]
[1, 5, 6, 9]
[6, 5, 1]
'''