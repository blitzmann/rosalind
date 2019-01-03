with open('rna_codon.txt') as file:
    lines = file.read().strip().split('\n')
    codons = {l[0]: l[1] for l in [line.strip().split(' ') for line in lines]}

with open('input.txt') as file:
    input = file.read().strip()
    chunks = [input[i:i + 3] for i in range(0, len(input ), 3)]
    print(''.join([codons[x] for x in chunks if codons[x] != 'Stop']))