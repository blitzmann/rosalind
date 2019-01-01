with open('input.txt') as file:
    a, b = tuple([int(x) for x in file.read().strip().split(' ')])
    print(a**2+b**2)
