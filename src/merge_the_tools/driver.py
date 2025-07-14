from src.merge_the_tools.utils import merge_the_tools

string = input('Enter string to check: ')
length= int(input('Enter length: '))
result = merge_the_tools(string, length)
print(result)