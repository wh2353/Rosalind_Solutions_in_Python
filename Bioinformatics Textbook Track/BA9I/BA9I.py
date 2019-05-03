'''
standard algorithm:
build a suffix matrix first,
sort each permutation
and return the last column of the sorted matrix
'''
def burrows_wheeler_transform(seq):
    double_seq = seq + seq 
    return ''.join(perm_seq[-1] for perm_seq in \
                   sorted([double_seq[i:i+len(seq)] for i in range(len(double_seq) - len(seq))]))

if __name__ == "__main__":
    
    seq = open("/Users/WENRUI/Downloads/rosalind_ba9i.txt","r").read().rstrip()
    print burrows_wheeler_transform(seq)