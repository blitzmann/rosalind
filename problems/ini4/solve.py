with open('input.txt') as file:
    a, b = tuple([int(x) for x in file.read().strip().split(' ')])
    print(sum([x for x in range(a, b+1) if x % 2 == 1]))