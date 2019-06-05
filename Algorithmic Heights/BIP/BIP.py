from collections import defaultdict

'''
Recursive algorithm to identify whether a graph is bipartite
Modified from Recursive Depth first search implementation (see CC.py)
The concept can be referred to the following link:
https://www.geeksforgeeks.org/check-if-a-given-graph-is-bipartite-using-dfs/
'''

def is_bipartite(adj_list, list_of_all_nodes, visited, color, node):
    
    visited[list_of_all_nodes.index(node)] = True
    
    temp_color = 0 - color[list_of_all_nodes.index(node)]
      
    for node_x in adj_list[node]:
        
        if not visited[list_of_all_nodes.index(node_x)]:
            color[list_of_all_nodes.index(node_x)] = temp_color
            '''
            if the subtree is not bipartite, return -1
            '''
            if is_bipartite(adj_list, list_of_all_nodes, visited, color, node_x) == -1:
                return -1
        
        elif visited[list_of_all_nodes.index(node_x)] and \
        color[list_of_all_nodes.index(node_x)] == color[list_of_all_nodes.index(node)]:
            return -1
    return 1      



if __name__ == "__main__":
    

    data_file = open("rosalind_bip.txt","r").read().rstrip().split("\n")
    number_samples = eval(data_file[0])
    
    all_ind = [i for i in range(len(data_file[1:])) if data_file[i] == '']
    
    for i in range(len(all_ind)):
        '''
        The first row is the total number of nodes and the total number of edges
        is NOT part of edge list, thus start_idx start from the empty row +2
        '''
        start_idx = all_ind[i] + 2
        if i == len(all_ind) - 1:
            end_idx = len(data_file)
        else:
            end_idx = all_ind[i+1]
            
        
        '''
        Build the adjacent list 
        and get the set for list_of_all_nodes for indexing purpose
        '''
        adj_list = defaultdict(list)
        list_of_all_nodes = set()
            
        for edge in data_file[start_idx: end_idx]:
            node1, node2 = [eval(x) for x in edge.split()]
            '''
            It is important that since the edges are undirected,
            edges from both directions need to be included in 
            the adjacent list
            '''
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
            list_of_all_nodes.add(node1)
            list_of_all_nodes.add(node2)
        
        list_of_all_nodes = list(list_of_all_nodes)    
        visited = [False]*(len(list_of_all_nodes))
        color = [0]*(len(list_of_all_nodes))
        node = list_of_all_nodes[0]
        color[0] = 1
        
        '''
        output result for each graph
        '''
        print is_bipartite(adj_list, list_of_all_nodes, visited, color, node),
       
    
    