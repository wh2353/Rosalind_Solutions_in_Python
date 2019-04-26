import numpy as np
from math import factorial
from numpy.linalg import matrix_power


'''
Read all parameters for the model and
build the transition matrix for Markov chain
'''
data_file = open("rosalind_foun.txt","r").read().rstrip().split("\n")
N, g = [eval(x) for x in data_file[0].split()]
k_vec = [eval(x) for x in data_file[1].split()]


transition_matrix = np.zeros((2*N+1, 2*N+1))

for i in range(2*N+1):
    for j in range(2*N+1):
        transition_matrix[i, j] = float(factorial(2*N))/ factorial(i) / factorial(2*N - i) * pow(float(j)/2/N, i) *\
        pow(1 - float(j)/2/N, 2*N - i)

'''
initialize the distribution vector matrix
of size k X (2N+1)
'''
k_matrix = np.zeros((len(k_vec), 2*N+1))
for i in range(len(k_vec)):
    k_matrix[i, k_vec[i]] = 1


'''
calculat the final distribution as dist_vec%*%power(transition_marix, g)
output log10 probability of each factor with zero recessive allele
'''
for i in range(1, g+1):
    final_dist_vec = (np.dot(matrix_power(transition_matrix, i), k_matrix.T))
    print ' '.join(str(x) for x in np.log10(final_dist_vec[0, -len(k_vec):]))