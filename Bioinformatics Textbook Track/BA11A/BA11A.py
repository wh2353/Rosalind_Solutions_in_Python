def mass_to_aa(val_x, protein_mass_table, epsilon):
    for key, value in protein_mass_table.iteritems():
        if abs(val_x - value) < epsilon:
            return key
    return ''

#input data preprocessing
data_file = open("rosalind_ba11a.txt","r").read().rstrip().split()
fragment_weights = [0] + [round(eval(x),5) for x in data_file]
#print fragment_weights

#get the protein mass table
protein_mass_table = open("protein_mass_table.txt","r").read().rstrip().split("\n")
protein_mass_table = dict((x.split()[0], int(eval(x.split()[1]))) for x in protein_mass_table)
#add X and Z to the table
protein_mass_table["X"]=4
protein_mass_table["Z"]=5



fragment_weights.sort()
epsilon = 0.1

for i in range(len(fragment_weights)):
    for j in range(i+1, len(fragment_weights)):
        aa = mass_to_aa(fragment_weights[j] - fragment_weights[i], protein_mass_table, epsilon)
        if aa:
            print str(int(fragment_weights[i])) + "->" + str(int(fragment_weights[j])) +":" + aa