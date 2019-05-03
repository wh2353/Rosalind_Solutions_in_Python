'''
Implement BetterBWMatching algorithm followed 
the pseudocode as described in problem BA9L and BA9M.
'''
def FirstOccurrence(first_col, symbol):
    return first_col.index(symbol)

def CountSymbol(end_idx, last_col, symbol):
    return last_col[:end_idx].count(symbol)
    
    

def BetterBWMMatching(last_col, pattern):
    top = 0
    bottom = len(last_col) - 1
    first_col = sorted(last_col)
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            segment = last_col[top:bottom+1]
            if symbol in segment:
                top = FirstOccurrence(first_col, symbol) + CountSymbol(top, last_col, symbol)
                bottom = FirstOccurrence(first_col, symbol) + CountSymbol(bottom + 1, last_col, symbol) - 1
            else:
                return 0
        else:
            return bottom - top + 1


if __name__ == "__main__":
    
    data_file = open("rosalind_ba9m.txt","r").read().rstrip().split("\n")
    seq = data_file[0]
    list_of_pattern = data_file[1].split()

    print ' '.join(str(BetterBWMMatching(seq, pattern)) for pattern in list_of_pattern)
        