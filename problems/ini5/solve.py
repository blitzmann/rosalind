with open('input.txt') as file:
    lines = [line for line in file]
    print(''.join([line for line in lines[1::2]]))