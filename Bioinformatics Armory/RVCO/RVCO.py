from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

'''
Function to identify Palindrome Sequences
'''
def isPalindromeSeq(seq):
    my_seq = Seq(seq, IUPAC.unambiguous_dna)
    return my_seq == my_seq.reverse_complement()


#read sequences and output results
data_file=open("rosalind_rvco.txt","r").read().rstrip().split(">")[1:]

list_of_seqs = map(lambda seq: "".join(seq.rstrip().split("\n")[1:]), data_file)

print sum(isPalindromeSeq(seq) for seq in list_of_seqs)