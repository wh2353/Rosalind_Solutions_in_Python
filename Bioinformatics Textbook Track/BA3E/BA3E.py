'''
The following function build a Debrujin ADJ based on list of kmers
'''
def DeBrujin_from_list_of_kmers(list_of_kmers):

    '''
    build the ADJ file using a dictionary of list
    '''
    DeBrujin_ADJ = defaultdict(list)

    for kmer in list_of_kmers:
        DeBrujin_ADJ[kmer[:-1]].append(kmer[1:])
        
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
    

    list_of_kmers = open("rosalind_ba3e.txt","r").read().rstrip().split("\n")
    
    DeBrujin_from_list_of_kmers(list_of_kmers)