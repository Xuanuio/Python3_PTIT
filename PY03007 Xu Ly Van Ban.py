import re
from sys import stdin

if __name__ == '__main__':
    doc = ''
    for line in stdin:
        doc += line.strip()
    sentences = re.split('[.?!]', doc)
    for sen in sentences:
        if len(sen) == 0: continue
        sen = sen.lower().split()
        sen[0] = sen[0][:1].upper() + sen[0][1:]
        print(' '.join(sen))