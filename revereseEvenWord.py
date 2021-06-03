string = 'zero one two three four five six seven eight nine'
words = string.split()
print(words)


for i in words:
    print(i)
    print(words.index(i))
    if(words.index(i) % 2 == 0):
        words[words.index(i)] = i[::-1]


result = ' '.join(words)
print(result)
