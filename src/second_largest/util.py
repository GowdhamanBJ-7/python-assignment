def second_largest(arr):

    set_value = list(set(arr))
    #setValue = list(set_value)
    set_value.sort(reverse=True)
    return set_value[1]
