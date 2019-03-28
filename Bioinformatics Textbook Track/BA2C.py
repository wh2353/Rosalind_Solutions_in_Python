import pandas as pd

def join_prob(kmer, prob_m):
    mul = 1
    for i in range(len(kmer)):
        mul *= eval(prob_m.loc[kmer[i], i])
    return mul

data_file = open("rosalind_ba2c.txt", "r").read().rstrip().split("\n")
seq = data_file[0]
k = eval(data_file[1])

prob_m = pd.DataFrame(map(lambda x: x.split(), data_file[2:]), index = ['A', 'C', 'G', 'T'])


list_of_kmers = [seq[i:i+k] for i in range(len(seq)-k+1)]

print max(list_of_kmers, key=lambda x: join_prob(x, prob_m))