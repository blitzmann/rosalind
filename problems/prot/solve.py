from problems.utils.rna_codons import codons2protein, rna2codons

with open('input.txt') as file:
    input = file.read().strip()
    print(codons2protein(rna2codons(input)))