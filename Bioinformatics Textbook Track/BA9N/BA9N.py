from collections import defaultdict

'''
Preprocessing
'''
data_file = open("rosalind_ba9n.txt","r").read().rstrip().split("\n")
seq = data_file[0]
list_of_patterns = data_file[1:]

kmer_dict = defaultdict(list)

k = len(list_of_patterns[0])

'''
Build a dictionary in which keys are kmers from the seqs and values are a list 
including all the starting position of that specific kmer
'''

for i in range(len(seq) - k + 1):
    kmer_dict[seq[i:i+k]].append(i)

'''
output results
'''    
for pattern in list_of_patterns:
    for i in kmer_dict[pattern]:
        print i,