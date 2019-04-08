import numpy as np
from collections import defaultdict

'''
Generate new centers as the mean of all the points in the same cluster
'''

def new_center_generator(data, centers):
    list_of_clusters = defaultdict(list)
    np_centers = np.array(centers)
    for each_data in data:
        each_data = np.array(each_data)
        list_of_clusters[((np_centers-each_data)*(np_centers-each_data)).sum(1).argmin()].append(each_data)
    return [sum(value) / float(len(value)) for key, value in list_of_clusters.iteritems()]

'''
Implement the LloydClustering algorithm
'''
def LloydClustering(data, centers):
    new_centers = new_center_generator(data, centers)
    while np.linalg.norm(np.array(new_centers) - np.array(centers)) != 0:
        centers = new_centers
        new_centers = new_center_generator(data, centers)
        
            

    return centers

if __name__ == "__main__":
    #data preprocessing
    data_file = map(lambda x: [eval(i) for i in x.split()], open("rosalind_ba8c.txt", "r").read().rstrip().split("\n"))
    k = data_file[0][0]
    m = data_file[0][1]
    data = data_file[1:]
    #first k points are selected as initial centers
    #comment out the following for random initialized centers
    #inital_centers = [data[i] for i in np.random.randint(0, len(data), k)]
    inital_centers = data[:k]
    final_centers = LloydClustering(data, inital_centers)
    
    for center in final_centers:
        print " ".join(map(lambda x: str(round(x,3)), center))
    