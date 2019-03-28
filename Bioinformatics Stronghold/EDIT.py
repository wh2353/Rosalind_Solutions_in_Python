import numpy as np
data_file=open("rosalind_edit.txt", "r").read().split(">")[1:]
list_of_seqs = map(lambda x: "".join(x.split()[1:]), data_file)
seq1 = list_of_seqs[0]
seq2 = list_of_seqs[1]
#initialize the alignment matrix
dp_matrix = np.zeros((len(seq1)+1, len(seq2)+1))
#filling the first row and first column
dp_matrix[0,1:] = range(1,len(seq2)+1)
dp_matrix[1:,0] = range(1,len(seq1)+1)

for i in range(1,len(seq1)+1):
    for j in range(1,len(seq2)+1):
        #if match delta = 0 otherwise delta = 1
        delta = int(not seq1[i-1] == seq2[j-1])
        #filing i,j element in dp_matrix
        dp_matrix[i,j] = min(dp_matrix[i-1, j]+1, dp_matrix[i-1, j-1]+delta, dp_matrix[i, j-1]+1)

#the edit distance is the element in the right bottom corner of the matrix            
print int(dp_matrix[len(seq1),len(seq2)])