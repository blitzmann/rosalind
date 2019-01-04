from problems.utils.fasta import parse
from problems.utils.funcs import trans_ratio

with open('input.txt') as file:
    input = file.read().strip()
    dna_lines = parse(input)
    print(trans_ratio(dna_lines[0][1], dna_lines[1][1]))