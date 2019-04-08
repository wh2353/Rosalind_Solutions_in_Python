import itertools
def hamming_distance(seq1, seq2):
    return sum(a!=b for [a, b] in zip(seq1, seq2))

def distance_cal(kmer, text):
    if kmer in text:
        return 0
    else:
        list_of_kmer = [text[i:i+len(kmer)] for i in range(len(text)-len(kmer)+1)]
        return min(hamming_distance(kmer, seq) for seq in list_of_kmer)

def final_dist(kmer, list_of_text):
    return sum(distance_cal(kmer, text) for text in list_of_text)



data_file = open ("rosalind_ba2h.txt", "r").read().rstrip().split('\n')
kmer = data_file[0]
list_of_seqs = data_file[1].split()

print final_dist(kmer, list_of_seqs)