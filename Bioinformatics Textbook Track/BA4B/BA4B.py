'''
get the reverse compliment of a given sequence
'''
def reverse_compliment(seq):
    return seq.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()[::-1]

'''
check whether a kmer can be translated into the given AA seq
'''

def is_kmer_match_aa(kmer, aa_seq, traDict):
    reverse_kmer = reverse_compliment(kmer)
    
    forward_seq = ''.join(traDict[kmer[3*i:(3*i+3)].replace('T', 'U')] for i in range(len(kmer)/3))
    reverse_seq = ''.join(traDict[reverse_kmer[3*i:(3*i+3)].replace('T', 'U')] for i in range(len(reverse_kmer)/3))
    
    if forward_seq == aa_seq or reverse_seq == aa_seq:
        return True
    return False
   
    
'''
read the AA codon table into a dictionary
'''
string = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

traL =  string.split()
traDict = dict(zip(traL[0::2], traL[1::2]))

#data preprocessing
data_file = open("rosalind_ba4b.txt","r").read().rstrip().split("\n")
DNA_seq = data_file[0]
AA_seq = data_file[1]

kmer_len = len(AA_seq)*3

'''
select kmers that can be translated into the given AA Seq
and output results in a proper format
'''
print '\n'.join(DNA_seq[i:i+kmer_len] for i in range(len(DNA_seq) - kmer_len + 1) \
                if is_kmer_match_aa(DNA_seq[i:i+kmer_len], AA_seq, traDict))