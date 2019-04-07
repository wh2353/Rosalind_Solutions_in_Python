#vectorized Greedy Motif Search Algorithm
import numpy as np
import time
def kmer2matrix(kmer):
    '''
    Covert a single k-mer to a (4, len(kmer)) binary matrix in the order of 'ACGT'.
    '''
    alphabet = 'ACGT'
    return np.array(map(lambda x: [int(x==letter) for letter in alphabet], kmer)).T

def matrix2kmer(m):
    '''
    Covert a (4, len(kmer)) binary k-mer matrix in the order of 'ACGT' back to DNA sequence.
    '''
    alphabet = 'ACGT'
    return ''.join([list(alphabet)[list(col).index(1)] for col in m.T ])

def most_likely_kmer_m(seq, k, prob_m):
    '''
    return the most likely kmer matrix
    '''
    list_of_kmer_m = [kmer2matrix(seq[i:i+k]) for i in range(len(seq)-k+1)]
    return max(list_of_kmer_m, key=lambda kmer_x: np.product(np.array(kmer_x*prob_m).sum(0)))

def score(list_of_motif_matrice):
    '''
    Returns the score of the dna list motifs.
    for each matching position of all kmers (column), 
    Calculate the min hamming distance between motif and [AAAAA, CCCCC, GGGGG, TTTTT]
    the final score will be the sum of distances of all columns
    Based on above, the following code take the most frequently matched base at each position,
    And the min hamming distance at that position will be the total number of kmers in the list
    minus the counts for the most frequent base
    '''
    return sum(len(list_of_motif_matrice)-np.amax(sum(list_of_motif_matrice).T, axis=1))

def GreedyMotifSearch(list_of_seqs, k, t):
    '''
    implement the GreadyMotifSearch Algorithm
    '''
    #initialize BestMotifs as the first k-mer of each string
    BestMotifs = [kmer2matrix(seq[:k]) for seq in list_of_seqs]
    #check each kmer in the first sequence
    list_of_kmers_in_first = [kmer2matrix(list_of_seqs[0][i:i+k]) for i in range(len(list_of_seqs[0])-k+1)]
    for kmer_m in list_of_kmers_in_first:
        tempMotifs = [kmer_m]
        for seq in list_of_seqs[1:]:
            prob_m = sum(tempMotifs)/ float(len(tempMotifs))
            tempMotifs += [most_likely_kmer_m(seq, k, prob_m)]
        
        if score(tempMotifs) < score(BestMotifs):
            BestMotifs = tempMotifs
            
    return [matrix2kmer(motif_m) for motif_m in BestMotifs]


if __name__ == "__main__":
    #read inputs
    start = time.time()
    data_file = open("rosalind_ba2d.txt").read().rstrip().split("\n")

    k = eval(data_file[0].split()[0])
    t = eval(data_file[0].split()[1])

    list_of_seqs = data_file[1:]

    #run GreedyMotifSearch function
    final_motifs = GreedyMotifSearch(list_of_seqs, k, t)
    for motif in final_motifs:
        print motif
    end = time.time()

    print "total time:" + str(end - start)
