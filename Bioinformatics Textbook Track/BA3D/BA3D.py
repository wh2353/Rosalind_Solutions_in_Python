'''
The following function build a Debrujin ADJ list from given sequence and kmer size
'''
def DeBrujin_ADJ_builder(seq, k):

    '''
    decompose into k-1 mers
    '''
    list_of_k_minus_one_mers = [seq[i:i+k-1] for i in range(len(seq) - k + 1 + 1)]

    '''
    build the ADJ file using a dictionary of list
    '''
    DeBrujin_ADJ = defaultdict(list)

    for i in range(len(seq) - k + 1):
        if list_of_k_minus_one_mers[i+1] not in DeBrujin_ADJ[list_of_k_minus_one_mers[i]]:
            DeBrujin_ADJ[list_of_k_minus_one_mers[i]].append(list_of_k_minus_one_mers[i+1])

    '''
    Output the ADJ file
    '''
    for key, value in DeBrujin_ADJ.iteritems():
        if len(value) > 1:
            print key + " -> " + ','.join(value)
        else:
            print key + " -> " + ''.join(value)

if __name__ == "__main__":

    from collections import defaultdict

    k, seq = open("rosalind_ba3d.txt","r").read().rstrip().split("\n")

    DeBrujin_ADJ_builder(seq, eval(k))