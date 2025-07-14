def merge_the_tools(string, k):
    result = []
    for i in range(0, len(string), k):
        split_string = string[i:i + k]
        seen = ''
        for c in split_string:
            if c not in seen:
                seen += c
        result.append(seen)
    return result


# def merge_the_tools(string, k):
#     result = []
#     for i in range(0, len(string), k):
#         split_string = string[i:i+k]
#         seen = ''
#         for c in split_string:
#             if c not in seen:
#                 seen += c
#         result.append(seen)
#         # s= ''.join(set(split_string))
#         # result.append(s)
#     return result
#
# print(merge_the_tools('AABCAAADA',3))


