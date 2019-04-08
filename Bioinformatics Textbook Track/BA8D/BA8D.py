import numpy as np
from scipy.spatial.distance import cdist



'''
Implement the soft k means clustering algorithm
'''
def SoftKmeansClustering(data, centers, beta, num_iters):
    for i in range(num_iters):
        #E step
        Z = np.exp(-beta*cdist(data, centers))
        Z /= Z.sum(axis=1, keepdims=True)
        #M Step
        centers = (np.dot(Z.T, data).T / Z.sum(0)).T

    return centers

if __name__ == "__main__":
    #data preprocessing
    data_file = map(lambda x: [eval(i) for i in x.split()], open("rosalind_ba8d.txt", "r").read().rstrip().split("\n"))
    k = data_file[0][0]
    m = data_file[0][1]
    beta = data_file[1][0]
    data = data_file[2:]
    #first k points are selected as initial centers
    #comment out the following for random initialized centers
    #inital_centers = [data[i] for i in np.random.randint(0, len(data), k)]
    initial_centers = data[:k]
    num_iters = 100 #suggested value in the problem description
    final_centers = SoftKmeansClustering(data, initial_centers, beta, num_iters)
    
    for center in final_centers:
        print " ".join(map(lambda x: str(round(x,3)), center))
    