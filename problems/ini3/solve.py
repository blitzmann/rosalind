with open('input.txt') as file:
    input, indicies = tuple(file.read().strip().split('\n'))
    a, b, c, d = tuple([int(x) for x in indicies.split(' ')])
    print("{} {}".format(input[a:b+1], input[c:d+1]))