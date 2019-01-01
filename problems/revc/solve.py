revc = {"A": "T", "T": "A", "G": "C", "C": "G"}

with open('input.txt') as file:
    input = file.read().strip()
    print(''.join([revc[x] for x in input])[::-1])