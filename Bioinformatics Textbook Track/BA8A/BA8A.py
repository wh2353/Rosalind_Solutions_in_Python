import numpy as np

'''
Return distance of each point
'''

def dist_each_data(each_data, centers):
    each_data = np.array(each_data)
    centers = np.array(centers)
    list_of_dists = ((centers-each_data)*(centers-each_data)).sum(1)
    return np.min(list_of_dists)

'''
Implement the FarthestFirstTraversal algorithm
'''
def FarthestFirstTraversal(data, k):

    #initialize the center as the first point in data
    centers = [data[0]]

    while len(centers) < k:
        centers += [max(data, key=lambda each_data: dist_each_data(each_data, centers))]

    return centers

if __name__ == "__main__":
    #data preprocessing
    data_file = map(lambda x: [eval(i) for i in x.split()], open("rosalind_ba8a.txt", "r").read().rstrip().split("\n"))
    k = data_file[0][0]
    m = data_file[0][1]
    data = data_file[1:]

    #identify centers and print them out
    centers = FarthestFirstTraversal(data, k)
    for center in centers:
        print " ".join(map(lambda x: str(x), center))
