
'''
The following is the function that 
converts peptide to peptide vector
'''
def peptide_to_vector(peptide, protein_mass_table):
    list_of_ind = [sum(protein_mass_table[letter] for letter in peptide[:i]) for i in range(len(peptide)+1)]
    return [int(idx+1 in list_of_ind) for idx in range(max(list_of_ind))]
    

    
if __name__ == "__main__":    
    #input data preprocessing
    AA_seq = open("rosalind_ba11c.txt","r").read().rstrip()
    

    #get the protein mass table
    protein_mass_table = open("protein_mass_table.txt","r").read().rstrip().split("\n")
    protein_mass_table = dict((x.split()[0], int(eval(x.split()[1]))) for x in protein_mass_table)
    #add X and Z to the table
    protein_mass_table["X"]=4
    protein_mass_table["Z"]=5
    
    #output the result
    print " ".join(map(lambda x: str(x), peptide_to_vector(AA_seq, protein_mass_table)))