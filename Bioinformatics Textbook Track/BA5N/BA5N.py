from collections import defaultdict

'''
Recursive method (modified from DFS) to perform tropological sorting
'''


def tropological_per_vertex(adj_list, list_of_all_nodes, visited, node, stack):
    
    visited[list_of_all_nodes.index(node)] = True
     
    for node_x in adj_list[node]:
        
        if not visited[list_of_all_nodes.index(node_x)]:
            
            tropological_per_vertex(adj_list, list_of_all_nodes, visited, node_x, stack)
    '''
    NOTE:
    stack = [node] + stack will not change the content in the actual stack 
    '''    
    
    #insert the parent node after all children having been inserted
    stack.insert(0, node)  
    
    
      
if __name__ == "__main__":
    
    data_file = open("rosalind_ba5n.txt","r").read().rstrip().split("\n")
        
    adj_list = defaultdict(list)
    list_of_all_nodes = set()
            
    for edge in data_file:
        node1, node2_list = [eval(x) for x in edge.split(" -> ")]
        #handle cases with multiple child nodes   
        try:
            for node2 in node2_list:
                adj_list[node1].append(node2)
                list_of_all_nodes.add(node2)
        except:
            adj_list[node1].append(node2_list)
            list_of_all_nodes.add(node2_list)
            
        list_of_all_nodes.add(node1)
        
        
    #the array list_of_all_nodes is used to map vertex to visited array
    list_of_all_nodes = list(list_of_all_nodes)    
        
    
        
    visited = [False]*(len(list_of_all_nodes))
    stack = []
    
    #sort all vertices with outgoing edges one by one
    for node in adj_list.keys():
        if not visited[list_of_all_nodes.index(node)]:
            tropological_per_vertex(adj_list, list_of_all_nodes, visited, node, stack)
                
    print ', '.join(str(x) for x in stack)