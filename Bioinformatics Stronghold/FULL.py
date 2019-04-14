#input data preprocessing
data_file = open("rosalind_full.txt","r").read().rstrip().split("\n")
full_weight = round(eval(data_file[0]),5)
fragment_weights = [round(eval(x),5) for x in data_file[1:]]


#get the protein mass table
protein_mass_table = open("protein_mass_table.txt","r").read().rstrip().split("\n")
protein_mass_table = dict((x.split()[0], eval(x.split()[1])) for x in protein_mass_table)


#identify the prefix and postfix pairs
#sort the fragment weights list first
fragment_weights.sort()
#error allowed
epsilon = 0.001
list_of_pairs = [[s1, s2] for s1 in fragment_weights[:(len(fragment_weights)/2)] for s2 in fragment_weights[(len(fragment_weights)/2):] if abs(s1 + s2 - full_weight) < epsilon]
output_AA = ''



'''
Iteratively test the first pairs to the second pair, 
if the difference is equal to a AA weight, remove the first pair
add that AA to the final string; otherwise, flip the second pair, 
add to the string, sort it, and repeat the process
'''
while len(list_of_pairs) > 1:
    
    if sum(abs(list_of_pairs[1][0] - list_of_pairs[0][0] - value) < epsilon for value in protein_mass_table.values()) != 0:
        for key, value in protein_mass_table.iteritems():
            
            if abs(value - list_of_pairs[1][0] + list_of_pairs[0][0]) < epsilon:
                output_AA += key
                break
        list_of_pairs.pop(0)
    
    else:
        list_of_pairs.append(list_of_pairs[1][::-1])
        list_of_pairs.pop(1)
    
    list_of_pairs.sort()
    
print output_AA
