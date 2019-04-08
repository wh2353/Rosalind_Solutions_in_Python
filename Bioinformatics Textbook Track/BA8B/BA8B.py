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
Calculate the Squared Error Distortion
'''
def SquaredErrorDistortion(data, centers):
    return sum(dist_each_data(each_data, centers) for each_data in data) / float(len(data))

    

if __name__ == "__main__":
    #data preprocessing
    data_file = open("rosalind_ba8b.txt", "r").read().rstrip().split("\n")
    data_file = [map(lambda x: eval(x), line.split())  for line in data_file if line != '--------']
    k = data_file[0][0]
    m = data_file[0][1]
    centers = data_file[1:k+1]
    data = data_file[k+1:]
    #output the result
    print SquaredErrorDistortion(data, centers)