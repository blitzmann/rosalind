data = '''
UUU F
CUU L
AUU I
GUU V
UUC F
CUC L
AUC I
GUC V
UUA L
CUA L
AUA I
GUA V
UUG L
CUG L
AUG M
GUG V
UCU S
CCU P
ACU T
GCU A
UCC S
CCC P
ACC T
GCC A
UCA S
CCA P
ACA T
GCA A
UCG S
CCG P
ACG T
GCG A
UAU Y
CAU H
AAU N
GAU D
UAC Y
CAC H
AAC N
GAC D
UAA Stop
CAA Q
AAA K
GAA E
UAG Stop
CAG Q
AAG K
GAG E
UGU C
CGU R
AGU S
GGU G
UGC C
CGC R
AGC S
GGC G
UGA Stop
CGA R
AGA R
GGA G
UGG W
CGG R
AGG R
GGG G
'''

lines = data.strip().split('\n')
codon_protein_mapping = {l[0]: l[1] for l in [line.strip().split(' ') for line in lines]}

def dna2rna(dna_str: str)->str:
    return dna_str.replace("T", "U")

def rna2codons(rna_str: str)->list:
    return [rna_str[i:i + 3] for i in range(0, len(rna_str), 3)]

def codons2protein(codons: list) -> str:
    return ''.join([codon_protein_mapping[x] for x in codons if codon_protein_mapping[x] != 'Stop'])
