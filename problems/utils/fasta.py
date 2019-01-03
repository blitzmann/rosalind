from typing import List

def parse(txt_block: str)->List[tuple]:
    # there's probably some clever regex that we can do here... but fuck it
    blocks = txt_block.strip().rsplit('>')[1:]

    return [(x[0], x[1].replace('\n','')) for x in [block.split('\n', 1) for block in blocks]]