with open('monoisotopic_mass.txt') as file:
    lines = file.read().strip().split('\n')
    weights = {l[0]: float(l[1]) for l in [line.strip().split(' ') for line in lines]}

with open('input.txt') as file:
    input = file.read().strip()
    print(''.join(str(round(sum([weights[x] for x in input]), 3))))