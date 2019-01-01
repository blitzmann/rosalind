from collections import Counter

with open('input.txt') as file:
    words = file.read().strip().split(' ')
    c = Counter(words)
    for k, v in c.items():
        print("{} {}".format(k, v))