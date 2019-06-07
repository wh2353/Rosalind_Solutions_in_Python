'''
Finding the longest repeat in the string
'''
import numpy as np
seq=open("rosalind_ba9d.txt", "r").read()
found = False

for k in range(len(seq)/2)[::-1]:
    list_of_kmers = [seq[i:i+k] for i in range(len(seq) - k + 1)]
    for kmer in list_of_kmers:
        if seq.count(kmer) > 1:
            print kmer
            found = True
            break
    if found:
        break