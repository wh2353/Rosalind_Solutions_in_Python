import numpy as np
import time
start = time.time()
data_files = open("rosalind_lcsq.txt", 'r').read().split(">")[1:]
seq1 = "".join(data_files[0].split("\n")[1:-1])
seq2 = "".join(data_files[1].split("\n")[1:-1])

m = len(seq1)
n = len(seq2)

#initialize a numpy matrix for recording potential matches

align_matrix = np.zeros(shape=(m,n))

for i in range(m):
    for j in range(n):
        if i == 0 or j == 0:
            align_matrix[i,j] = int(seq1[i]==seq2[j])

        elif seq1[i]==seq2[j]:
            align_matrix[i,j] = align_matrix[i-1,j-1] + 1
        else:
            align_matrix[i,j] = max(align_matrix[i-1,j], align_matrix[i,j-1])

#read the longest common subsequence from the align_matrix

output_str = []

[a, b] = np.argwhere(align_matrix == align_matrix.max())[0]

while a>=0 and b >=0:

    if seq1[a] == seq2[b]:
        output_str.append(seq1[a])
        a = a -1
        b = b -1
    elif align_matrix[a-1, b] > align_matrix[a, b-1]:
        a = a-1
        b = b
    else:
        a = a
        b = b -1

print "".join(output_str[::-1])

end = time.time()
print end-start