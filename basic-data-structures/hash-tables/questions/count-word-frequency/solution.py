def word_frequency(text):
    freq = {}
    for word in text.split():
        freq[word] = freq.get(word, 0) + 1
    return freq


print(word_frequency("this is a test this is only a test"))
# {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
