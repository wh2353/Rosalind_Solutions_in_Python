import numpy as np

'''
Implementations to check whether there is any square (length 4 path) in the graph

First of all, the (i,j) element of the N's Power of an adjacent matrix equal to the 
total number of walks of length N from node i to node j, which can be proved through 
induction (see https://core.ac.uk/download/pdf/141678246.pdf, theorem 0.1). It is also
worth noting that length N walks is NOT equivalent to length N Paths, as walks allow 
repetitions on the same edge while paths do not. Thus, the 4th power of an adjacent matrix 
only tells the total number of walks of length 4 rather than paths of length 4, and it is 
difficult to subtract the number of walks with repetitive edges from the total number

Alternatively, we can first calculate the the number of length 2 walks from i to j,
and the total number of length 2 walks has to be equal to number of length 2 paths if i is NOT
equal to j. If there are more than 1 DISTINCT length 2 paths between i and j, then there must
have a square. If none of the distinct is and js have more than 1 distinct length 2 paths/walks,
there is no squares exist in the graph

'''

def has_square(adj_matrix):
    
    len_of_walk = 2
    A_squared_diag_zero = np.linalg.matrix_power(adj_matrix, len_of_walk)
    np.fill_diagonal(A_squared_diag_zero, 0)
    
    if np.any(A_squared_diag_zero > 1):
        return 1
    return -1



if __name__ == "__main__":
    

    data_file = open("rosalind_sq.txt","r").read().rstrip().split("\n")
    number_samples = eval(data_file[0])
    
    
    
    all_ind = [i for i in range(len(data_file[1:])) if data_file[i] == '']
    
    for i in range(len(all_ind)):
        '''
        The first row is the total number of nodes and the total number of edges
        is NOT part of edge list, thus start_idx start from the empty row +2
        '''
        N, E = [eval(x) for x in data_file[all_ind[i] + 1].split()]
        start_idx = all_ind[i] + 2
        if i == len(all_ind) - 1:
            end_idx = len(data_file)
        else:
            end_idx = all_ind[i+1]
            
        
        '''
        Build the adjacent matrix
        '''
        adj_matrix = np.zeros((N, N))
        
            
        for edge in data_file[start_idx: end_idx]:
            node1, node2 = [eval(x) for x in edge.split()]
            '''
            It is important that since the edges are undirected,
            edges from both directions need to be included in 
            the adjacent list
            '''
            adj_matrix[node1-1, node2-1] += 1
            adj_matrix[node2-1, node1-1] += 1
        
        #print adj_matrix
        '''
        output result for each graph
        '''
        print has_square(adj_matrix),
       
