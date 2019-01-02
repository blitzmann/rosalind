with open('input.txt') as file:
    s, t = file.read().strip().split('\n')
    count = 0
    for i, c in enumerate(s):
        count += 1 if s[i] != t[i] else 0
    print(count)
