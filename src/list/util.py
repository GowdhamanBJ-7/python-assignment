def process_commands(N, commands):
    result = []
    list1 = []
    for i in range(N):
        command = commands[i].split()
        cmd = command[0]
        if cmd == 'insert':
            list1.insert(int(command[1]), int(command[2]))
        elif cmd == 'append':
            list1.append(int(command[1]))
        elif cmd == 'remove':
            list1.remove(int(command[1]))
        elif cmd == 'sort':
            list1.sort()
        elif cmd == 'pop':
            list1.pop()
        elif cmd == 'reverse':
            list1.reverse()
        elif cmd == 'print':
            result.append(list1.copy())
    return result
