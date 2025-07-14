def mutate_string(string, position, character):
    input_string = list(string)
    input_string[position] = character
    output = ''.join(input_string)
    return output

