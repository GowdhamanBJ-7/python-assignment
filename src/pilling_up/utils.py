from collections import deque

def can_stack(cubes):
    dq = deque(cubes)
    top = float('inf')

    while dq:
        if dq[0] >= dq[-1]:
            pick = dq.popleft()
        else:
            pick = dq.pop()

        if pick > top:
            return "No"
        top = pick

    return "Yes"

# Input Reading
T = int(input())
for _ in range(T):
    n = int(input())
    cubes = list(map(int, input().split()))
    print(can_stack(cubes))
