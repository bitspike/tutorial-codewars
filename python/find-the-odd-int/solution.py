import collections

def find_it(seq):
    c = collections.Counter(seq)
    for i in c:
        if c[i] % 2 == 1:
            return i