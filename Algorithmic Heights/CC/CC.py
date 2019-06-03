from collections import defaultdict
'''
Recursive algorithm for DFS
'''
def Depth_first_search(adj_list, visited, node):
    visited[node] = True
    for node_x in adj_list[node]:
        if not visited[node_x]:
            Depth_first_search(adj_list, visited, node_x)
            
'''
Find total number of connected components using DFS
'''
def Connected_components_counter(adj_list):
    total_num = 0
    #make sure the indice of the array visited is the same as the name of nodes
    visited = [False]*(len(adj_list)+1)
    for i in adj_list.keys():
        if not visited[i]:
            total_num += 1
            Depth_first_search(adj_list, visited, i)
    return total_num

if __name__ == "__main__":

    data_file = open("rosalind_cc.txt","r").read().rstrip().split("\n")
    N, E = [eval(x) for x in data_file[0].split()]

    adj_list = defaultdict(list)

    
    #build adjacent list from edge file
    for node in range(1, N+1):
        adj_list[node] = []

    for edge in data_file[1:]:
        node1, node2 = [eval(x) for x in edge.split()]
        '''
        It is important that since the edges are undirected,
        edges from both directions need to be included in 
        the adjacent list
        '''
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    #output result
    print Connected_components_counter(adj_list)    

