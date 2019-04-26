'''
Read the protein mass table
'''
protein_mass_table = open("protein_mass_table.txt","r").read().rstrip().split("\n")
protein_mass_table = dict((x.split()[0], int(eval(x.split()[1]))) for x in protein_mass_table)
'''
Get the unique mass values
for two AAs with the same weight, Rosalind actually consider them as the same solution
That is so wroooooong
'''
list_of_AA_mass = set(protein_mass_table.values())


'''
Read total mass and run dp to get the total number of combinations.
The algorithm is similar to question BA5A
'''
total_mass = eval(open("rosalind_ba4d.txt","r").read().rstrip())

dp_vec = [0]*(total_mass+1)
dp_vec[0] = 1


for i in range(total_mass+1):
    for aa in list_of_AA_mass:
        if i >= aa:
            dp_vec[i] += dp_vec[i-aa]
            
print dp_vec[total_mass]
