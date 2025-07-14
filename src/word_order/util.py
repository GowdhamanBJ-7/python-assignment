def count_words(word):
    set_value = {}
    unique_word = []
    for ch in word:
        if ch in set_value:
            set_value[ch] += 1
        else:
            set_value[ch] = 1

    #unique word length
    #print(len(set(word)))

    for i in set_value.values():
        unique_word.append(i)

    return len(set(word)), unique_word
