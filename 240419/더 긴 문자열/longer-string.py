words = list(map(str, input().split()))

if len(words[0]) < len(words[1]):
    print(words[1], len(words[1]))
elif len(words[1]) < len(words[0]):
    print(words[0], len(words[0]))
else:
    print('same')