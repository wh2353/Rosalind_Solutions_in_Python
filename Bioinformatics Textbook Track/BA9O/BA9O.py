import time
from collections import defaultdict
import numpy as np
import itertools

'''
The kmer2vector function converts a k-mer into a length = 4*K binary vector
'''

def kmer2vector(kmer):
    template = ['A', 'C', 'G', 'T']
    return list(itertools.chain.from_iterable([int(letter == base) for base in template] for letter in kmer))    
    
'''
Vectorized algorithm to identify starting matching positions with hamming distance < d
The hamming_d_matrix is a n*l matrix, in which row indices are matching positions in 
the original seq and column indices are indices of corresponding patterns that need to 
be checked, the row indices for each column with value <= d are returned
'''    

def find_match_indice(seq, list_of_kmers, d):
    return_vec = []
    
    '''
    Cluster kmers based on corresponding size 
    '''
    kmer_groups_by_length = defaultdict(list)
    for kmer in list_of_kmers:
        kmer_groups_by_length[len(kmer)].append(kmer)
    
    '''
    Process clusters of same size kmers one by one 
    and return matching indices
    '''
    
    for kmer_len, kmer_group in kmer_groups_by_length.iteritems():
        kmer_matrix = np.matrix([kmer2vector(kmer) for kmer in kmer_group])
        seq_matrix = np.matrix([kmer2vector(kmer) for kmer in [seq[i:i+kmer_len] for i in range(len(seq) - kmer_len + 1)]])
        hamming_d_matrix = kmer_len - np.dot(seq_matrix, kmer_matrix.T)
        return_vec.append(np.where(hamming_d_matrix <= d)[0])
    
    return sorted(list(itertools.chain.from_iterable(return_vec)))
    
    
if __name__ == "__main__":
    
    start = time.time()
    '''
    Preprocessing
    '''
    data_file = open("rosalind_ba9o.txt","r").read().rstrip().split("\n")
    seq = data_file[0]

    list_of_kmers = data_file[1].split()
    d = eval(data_file[2])

    '''
    obtain matching indice and output them into a right format
    '''

    print ' '.join(str(i) for i in find_match_indice(seq, list_of_kmers, d))

    '''
    Count total running time in seconds
    '''
    end = time.time()

    print "total running time: " + str(round(end - start, 3)) + " seconds"