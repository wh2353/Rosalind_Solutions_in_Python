'''
return suffix index of a sequence
'''
def suffix_index(seq):
    list_of_suffix = [seq[i:] for i in range(len(seq))]
    return sorted(range(len(list_of_suffix)), key = lambda i: list_of_suffix[i])

if __name__ == "__main__":
    seq = open("rosalind_ba9g.txt","r").read().rstrip()

    print ', '.join(str(i) for i in suffix_index(seq))