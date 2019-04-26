import numpy as np
from math import factorial
from numpy.linalg import matrix_power


'''
Read all parameters for the model and
build the transition matrix for Markov chain
'''
N, m, g, k = map(lambda x: eval(x), open("rosalind_wfmd.txt","r").read().rstrip().split())
transition_matrix = np.zeros((2*N+1, 2*N+1))

for i in range(2*N+1):
    for j in range(2*N+1):
        transition_matrix[i, j] = factorial(2*N) / factorial(i) / factorial(2*N - i) * pow(float(j)/2/N, i) *\
        pow(1 - float(j)/2/N, 2*N - i)

'''
initialize the distribution vector
'''
dist_vec = [0]*(2*N+1)
dist_vec [2*N-m]= 1



'''
calculat the final distribution as dist_vec%*%power(transition_marix, g)
output prob of at least k recessive allels
'''
final_dist_vec = np.dot(matrix_power(transition_matrix, g), np.array(dist_vec))
print 1 - sum(final_dist_vec[0:k])