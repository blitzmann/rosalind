import re

with open('input.txt') as file:
    s, t = file.read().strip().split('\n')
    regex = r"(?=({}))".format(t)
    matches = re.finditer(regex, s)
    print(' '.join([str(x.start() + 1) for x in matches]))
