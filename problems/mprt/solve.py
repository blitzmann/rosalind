import requests
import re

regex = r"(?=N[^P][ST][^P])"  # N-glycosylation motif

with open('input.txt') as file:
    for id in [line.strip() for line in file]:
        req = requests.get('http://www.uniprot.org/uniprot/{}.fasta'.format(id))
        data = req.text.split('\n')
        string = ''.join([x for x in data[1:]])  # don't take first line
        matches = re.finditer(regex, string)
        positions = [str(m.start() + 1) for m in matches]
        if len(positions) == 0:
            continue

        print(id)
        print(' '.join(positions))

