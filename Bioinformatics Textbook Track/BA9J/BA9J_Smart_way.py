'''
Smart Way of implementing BWT reversal:
instead of indexing letters from first and last column,
let first column equal to range(len(seq)), then sorted
alphabetically based on the letters in the input seq, the
index and the content of the first column can be served as 
the previous first and last column
'''
def burrows_wheeler_reverse(seq):
    out_seq = ''
    idx = 0
    first_col = sorted(range(len(seq)), key= lambda i: seq[i])
    while len(out_seq) < len(seq):
        out_seq += seq[first_col[idx]]
        idx = first_col[idx]
    return out_seq[1:] + out_seq[0]


if __name__ == "__main__":
    
    seq = open("rosalind_ba9j.txt","r").read().rstrip()

    print burrows_wheeler_reverse(seq)

