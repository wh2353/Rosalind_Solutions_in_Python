from collections import defaultdict
data_file = open("rosalind_ba9b.txt","r").read().rstrip().split("\n")
seq = data_file[0]
list_of_kmers = data_file[1:]

seq_dict = defaultdict(list)

k = len(list_of_kmers[0])

for i in range(len(seq) - k + 1):
    
    seq_dict[seq[i:i+k]].append(i)
    
for kmer in list_of_kmers:
    for i in seq_dict[kmer]:
        print i,