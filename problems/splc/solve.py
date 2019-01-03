import re
from problems.utils.rna_codons import rna2codons, codons2protein, dna2rna
from problems.utils.fasta import parse


with open('input.txt') as file:
    input = file.read().strip()
    dna_lines = parse(input)
    dna = dna_lines[0][1]

    for _, introns in dna_lines[1:]:
        dna = dna.replace(introns, '')

    print(codons2protein(rna2codons(dna2rna(dna))))