with open('input.txt') as file:
    input = file.read()

print("{} {} {} {}".format(input.count('A'), input.count('C'), input.count('G'), input.count('T')))