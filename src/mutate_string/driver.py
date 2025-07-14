from src.mutate_string.utils import mutate_string

string = input('Enter string: ')
position= int(input('Enter position: '))
letter = input('Enter character to replace: ')
result = mutate_string('abracadabra', 5, 'k')
print(result)

'''
sample input
string: 'abracadabra', 
position: 5,
letter: 'k'
'''

'''
sample output

abrackdabra
'''