'''
The following code finds the hamming distance between a kmer and a list of sequences
'''

def hamming_dist(kmer_x, kmer_y):
    return(sum(a!=b for a, b in zip(kmer_x, kmer_y)))

def hamming_to_sequence(kmer, seq):
    k = len(kmer)
    return min(hamming_dist(seq[i:i+k], kmer) for i in range(len(seq) -k + 1))

if __name__ == "__main__":
    data_file=open("rosalind_ba2h.txt", "r").read().split()

    kmer = data_file[0]
    list_of_seqs = data_file[1:]

    print sum(hamming_to_sequence(kmer, seq) for seq in list_of_seqs)