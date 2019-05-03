'''
LastToFirst function based on the
index sorting implementation of BWT reversal 
see Problem BA9J
'''
def LastToFirst(seq, idx_last):
    return sorted(range(len(seq)), key= lambda i: seq[i]).index(idx_last)

if __name__ == "__main__":

    data_file = open("rosalind_ba9k.txt","r").read().rstrip().split("\n")
    seq = data_file[0]
    idx = eval(data_file[1])

    print LastToFirst(seq, idx)