from src.word_order.util import count_words

w = int(input())
word = list(input().strip() for _ in range(w))

unique_count, word_count = count_words(word)

print(unique_count,  word_count)

'''
sample input

4
bcdef
abcdefg
bcde
bcdef
'''
'''
Sample Output

3
2 1 1
'''