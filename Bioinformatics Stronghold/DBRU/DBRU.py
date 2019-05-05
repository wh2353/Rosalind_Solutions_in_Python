'''
Function for reverse compliment a DNA seq
'''

def reverse_compliment(seq):
    return seq.replace('A', 't').replace('C', 'g').replace('G', 'c').replace('T', 'a').upper()[::-1]

'''
The following function build a Debrujin ADJ list from given list of kmers
'''
def DeBrujin_from_list_of_kmers(list_of_kmers):

   
   

    '''
    build the ADJ file using a dictionary of list
    '''
    DeBrujin_ADJ = defaultdict(list)

    for kmer in list_of_kmers:
        if kmer[1:] != DeBrujin_ADJ[kmer[:-1]]:
            DeBrujin_ADJ[kmer[:-1]].append(kmer[1:])
        
    '''
    Output the ADJ file
    '''
    for key, value in DeBrujin_ADJ.iteritems():
        for x in value:
            print "(" + key + ", " + x + ")"




if __name__ == "__main__":

    from collections import defaultdict
    

    list_of_kmers = open("rosalind_dbru.txt","r").read().rstrip().split("\n")
    
    list_of_kmers += [reverse_compliment(kmer) for kmer in list_of_kmers]
    
    DeBrujin_from_list_of_kmers(set(list_of_kmers))
    

