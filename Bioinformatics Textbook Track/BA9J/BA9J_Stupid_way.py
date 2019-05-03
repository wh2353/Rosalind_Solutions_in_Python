'''
Standard (but Stupid) way to recover the original seq
with rank each letter in the BWT string, build 
the indexed first and last column, combined them
into a dictionary, and map the original string from
the dictionary
'''
def return_seq(first_and_last_column, element):
    orig_seq = '$'
    while first_and_last_column[element] != '$':
        orig_seq = first_and_last_column[element] + orig_seq
        element = first_and_last_column[element]
    return orig_seq


def last_to_first_with_idx(last_column):
    first_with_no_idx = sorted(x[0] for x in last_column)
    return ['$'] + [first_with_no_idx[i] + str(first_with_no_idx[:i+1].count(first_with_no_idx[i]))\
                         for i in range(1, len(first_with_no_idx))]

def burrows_wheeler_reverse(seq):
    last_column = []
    for i in range(len(seq)):
        if seq[i] == '$':
            last_column.append('$')
        else:
            last_column.append(seq[i]+str(seq[:i+1].count(seq[i])))
    first_column = last_to_first_with_idx(last_column)
    first_and_last_column = dict(zip(first_column, last_column))
    
    return ''.join(x for x in return_seq(first_and_last_column, "$") if not x.isdigit())
    

if __name__ == "__main__":
    
    seq = open("rosalind_ba9j.txt","r").read().rstrip()
    print burrows_wheeler_reverse(seq)