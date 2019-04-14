import collections

'''
Get the weights of all prefix and postfix for a specific AA seq, 
and return the max multiplicity of R_set-AA_set
'''
def max_multiplicity(seq, R_set, protein_mass_table):
    weight_of_all_prefix = [sum(protein_mass_table[AA] for AA in seq[i:]) for i in range(len(seq))]
    weight_of_all_postfix = [sum(protein_mass_table[AA] for AA in seq[:-i]) for i in range(len(seq))]
    AA_set = weight_of_all_prefix + weight_of_all_postfix
    return collections.Counter([round(val1 - val2, 6) for val1 in R_set for val2 in AA_set]).most_common(1)[0][1]


#input data preprocessing
data_file = open("rosalind_prsm.txt","r").read().rstrip().split("\n")
n = eval(data_file[0])
list_of_seqs = data_file[1:1+n]
R_set = [eval(x) for x in data_file[1+n:]]

#get the protein mass table
protein_mass_table = open("/Users/WENRUI/Downloads/protein_mass_table.txt","r").read().rstrip().split("\n")
protein_mass_table = dict((x.split()[0], eval(x.split()[1])) for x in protein_mass_table)

#output the result
seqs_dict = dict(zip(list_of_seqs, [max_multiplicity(seq, R_set, protein_mass_table) for seq in list_of_seqs]))
print max(seqs_dict.values())
print max(seqs_dict, key=seqs_dict.get)