'''
The following function converts mass to corresponding amino acid
'''


def mass_to_aa(val_x, protein_mass_table, epsilon):
    for key, value in protein_mass_table.iteritems():
        if abs(val_x - value) < epsilon:
            return key
    return ''


'''
The following is the function that 
converts peptide vector to peptide
'''
def vector_to_peptide(vector, protein_mass_table, epsilon):
    list_of_weights = [0] + [i+1 for i in range(len(vector)) if vector[i] == 1]
    
    return "".join(mass_to_aa(list_of_weights[i] - list_of_weights[i-1], protein_mass_table, epsilon) for i in range(1, len(list_of_weights)))
    

    
if __name__ == "__main__":    
    #input data preprocessing
    peptide_vector = map(lambda x: int(x), open("rosalind_ba11d.txt","r").read().rstrip().split())
    #print peptide_vector

    #get the protein mass table
    protein_mass_table = open("protein_mass_table.txt","r").read().rstrip().split("\n")
    protein_mass_table = dict((x.split()[0], int(eval(x.split()[1]))) for x in protein_mass_table)
    #add X and Z to the table
    protein_mass_table["X"]=4
    protein_mass_table["Z"]=5
    
    #set threshold for error
    epsilon = 0.1
    #output the result
    print vector_to_peptide(peptide_vector, protein_mass_table, epsilon)