from collections import defaultdict

'''
Recursive method (modified from DFS) to check acyclicity of a graph
'''


def is_Acyclicity(adj_list, list_of_all_nodes, visited, node):
    
    visited[list_of_all_nodes.index(node)] = True
     
    for node_x in adj_list[node]:
        
        if not visited[list_of_all_nodes.index(node_x)]:
            
            '''
            check the Acyclicity of the subtree
            '''
            if is_Acyclicity(adj_list, list_of_all_nodes, visited, node_x) == -1:
                return -1
        
        elif visited[list_of_all_nodes.index(node_x)]:
            return -1
    return 1  
    
    
      
if __name__ == "__main__":
    data_file = open("rosalind_dag.txt","r").read().rstrip().split("\n")
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
            
            adj_list[node1].append(node2)
            
            list_of_all_nodes.add(node1)
            list_of_all_nodes.add(node2)
        
        list_of_all_nodes = list(list_of_all_nodes)    
        
        
        '''
        Defaultdict will automatically add 
        keys with empty value into dictionary
        I have to get rid of these empty entries
        or otherwise the algorithm will not work
        THIS IS SUPER ANNOYING
        '''
        #remove empty values from dictionary
        for key in adj_list.keys():
            if len(adj_list[key]) == 0:
                del(adj_list[key])
        
        
        visited = [False]*(len(list_of_all_nodes))
        
        node = adj_list.keys()[0]
        print is_Acyclicity(adj_list, list_of_all_nodes, visited, node),
        
        