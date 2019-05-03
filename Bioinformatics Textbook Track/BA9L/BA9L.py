'''
Implement BWMatching algorithm followed 
the pseudocode as described in problem BA9L.
the LastToFirst function implemented
in problem BA9K is also utilized
'''
def LastToFirst(seq, idx_last):
    return sorted(range(len(seq)), key= lambda i: seq[i]).index(idx_last)


def BWMMatching(last_col, pattern):
    top = 0
    bottom = len(last_col) - 1
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            segment = last_col[top:bottom+1]
            if symbol in segment:
                '''
                add top index to obtain the index of the symbol in the seq
                that is also within the interval [top, bottom]
                '''
                topIndex = segment.index(symbol) + top
                bottomIndex = len(segment) - 1 - segment[::-1].index(symbol) + top
                top = LastToFirst(last_col, topIndex)
                bottom = LastToFirst(last_col, bottomIndex)
            else:
                return 0
        else:
            return bottom - top + 1


if __name__ == "__main__":
    
    data_file = open("rosalind_ba9l.txt","r").read().rstrip().split("\n")
    seq = data_file[0]
    list_of_pattern = data_file[1].split()

    print ' '.join(str(BWMMatching(seq, pattern)) for pattern in list_of_pattern)
        