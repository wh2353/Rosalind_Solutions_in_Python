'''
This quesiton is almost identical to problem "FULL"
in Bioinformatics Stronghold
'''

'''
Function that converts mass to corresponding AA
'''
def mass_to_aa(val_x, protein_mass_table, epsilon):
    for key, value in protein_mass_table.iteritems():
        if abs(val_x - value) < epsilon:
            return key
    return ''

#input data preprocessing
data_file = open("rosalind_ba11b.txt","r").read().rstrip().split()
fragment_weights = [0]+[int(eval(x)) for x in data_file]

#get the protein mass table
protein_mass_table = open("protein_mass_table.txt","r").read().rstrip().split("\n")
protein_mass_table = dict((x.split()[0], int(eval(x.split()[1]))) for x in protein_mass_table)
#add X and Z to the table
protein_mass_table["X"]=4
protein_mass_table["Z"]=5

#identify the prefix and postfix pairs
#sort the fragment weights list first
fragment_weights.sort()

full_weight = fragment_weights[0] + fragment_weights[-1]
#error allowed
epsilon = 1
list_of_pairs = [[s1, s2] for s1 in fragment_weights[:(len(fragment_weights)/2)] for s2 in fragment_weights[(len(fragment_weights)/2):] if abs(s1 + s2 - full_weight) < epsilon]
output_AA = ''


'''
Iteratively test the first pairs to the second pair, 
if the difference is equal to a AA weight, remove the first pair
add that AA to the final string; otherwise, flip the second pair, 
add to the string, sort it, and repeat the process
'''
while len(list_of_pairs) > 1:
    aa = mass_to_aa(abs(list_of_pairs[1][0] - list_of_pairs[0][0]), protein_mass_table, epsilon)
    if aa: #if aa is a AA, if aa will be true

        output_AA += aa
        list_of_pairs.pop(0)

    else:
        list_of_pairs.append(list_of_pairs[1][::-1])
        list_of_pairs.pop(1)
    list_of_pairs.sort()

#append the last AA and output the final string    
print output_AA + mass_to_aa(min(list_of_pairs[0]), protein_mass_table, epsilon)