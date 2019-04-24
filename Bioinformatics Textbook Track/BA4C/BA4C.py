from collections import Counter
'''
Calculate the protein mass
'''
def protein_mass_calculator(AA, protein_mass_table):
    return sum(protein_mass_table[aa] for aa in AA)


'''
Read the protein mass table
'''
protein_mass_table = open("protein_mass_table.txt","r").read().rstrip().split("\n")
protein_mass_table = dict((x.split()[0], int(eval(x.split()[1]))) for x in protein_mass_table)


'''
repeat the AA sequence to count for circular subsequences
'''
AA_seq = open("rosalind_ba4c.txt","r").read().rstrip().split("\n")[0]
elongated_seq = AA_seq + AA_seq
list_of_all_fragments = [AA_seq]
for kmer_len in range(1, len(AA_seq)):
    list_of_all_fragments += [elongated_seq[i:i+kmer_len] for i in range(len(elongated_seq) - kmer_len + 1)]
    

'''
Set the number of repetitions for each subsequence based on its frequency 
'''    
freq_of_framents = Counter(list_of_all_fragments)

selected_fragments = ['']

for key, value in freq_of_framents.iteritems():
    if value % 2 == 1:
        selected_fragments += [key]
    else:
        selected_fragments += [key]*(value/2)


'''
Calculate the mass, sort and output the result
'''        
output_vec  = [protein_mass_calculator(AA, protein_mass_table) for AA in selected_fragments]
output_vec.sort()

print ' '.join(str(x) for x in output_vec)
