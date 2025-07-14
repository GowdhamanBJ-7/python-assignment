def noIdea(arr, A, B):
    happiness = sum((i in A) - (i in B) for i in arr)
    return happiness

# (1 in A) - (1 in B) = 1 - 0 = +1
# (5 in A) - (5 in B) = 0 - 1 = -1
# (3 in A) - (3 in B) = 1 - 0 = +1
