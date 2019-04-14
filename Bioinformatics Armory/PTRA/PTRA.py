from Bio.Seq import translate, CodonTable

data_file=open("rosalind_ptra.txt","r").read().rstrip().split("\n")
DNA_seq = data_file[0]
AA_seq = data_file[1]


for code in CodonTable.ambiguous_generic_by_id.keys():
    
    if translate(DNA_seq, table=code, to_stop=True) == AA_seq:
        print code
        break