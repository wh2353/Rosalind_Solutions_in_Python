def is_negative_cycle(nodes_and_edges_weights):
    num_of_nodes = eval(nodes_and_edges_weights[0][0])
    num_of_edges = eval(nodes_and_edges_weights[0][1])
    #remove the first line (num of nodes and edges information from the nodes and edges list)
    nodes_and_edges_weights.pop(0)
    all_nodes = map(lambda x:str(x), range(1, num_of_nodes+1))


    #Bellman-ford Algorithm Initialization
    #set distance to a very large int 0xFFFFF
    dist_to_s = dict(zip(all_nodes, [0xFFFFF]*len(all_nodes)))
    start_node = "1"
    dist_to_s[start_node] = 0


    #Bellman-ford relax each edge |V|-1 times to make sure each nodes have the shortest path to the source
    for i in range(1, len(all_nodes)-1):
        for edge_with_weight in nodes_and_edges_weights:
            [u, v, w] = [edge_with_weight[0], edge_with_weight[1], eval(edge_with_weight[2])]
            if dist_to_s[v] > dist_to_s[u] + w:
                dist_to_s[v] = dist_to_s[u] + w
    
    #check to make sure there is no negative cycle
    for edge_with_weight in nodes_and_edges_weights:
        [u, v, w] = [edge_with_weight[0], edge_with_weight[1], eval(edge_with_weight[2])]
        if dist_to_s[v] > dist_to_s[u] + w:
            return 1
    return -1
    
#preprocess the data and build a adjacent list
graph_info = map(lambda x: [str(i) for i in x.split()], open("rosalind_nwc.txt", "r").read().split("\n")[:-1])
number_of_graph = graph_info[0]
all_graph_indice = [key for key, value in enumerate(graph_info) if len(value) == 2]
#check all but the last graph
for i in range(len(all_graph_indice)-1):
    print is_negative_cycle(graph_info[all_graph_indice[i]: all_graph_indice[i+1]]),
#check the last graph
print is_negative_cycle(graph_info[all_graph_indice[-1]:])