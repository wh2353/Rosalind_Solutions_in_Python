from collections import defaultdict
#preprocess the data and build a adjacent list
nodes_and_edges_weights = map(lambda x: [str(i) for i in x.split()], open("rosalind_dij.txt", "r").read().split("\n")[:-1])
#get num of nodes and num of edges
num_of_nodes = eval(nodes_and_edges_weights[0][0])
num_of_edges = eval(nodes_and_edges_weights[0][1])
#remove the first line (num of nodes and edges information from the nodes and edges list)
nodes_and_edges_weights.pop(0)

#build the adjacent list
all_nodes = map(lambda x:str(x), range(1, num_of_nodes+1))

adjacent_list = defaultdict(list)

for node in all_nodes:
    for edge in nodes_and_edges_weights:
        if edge[0] == node:
            adjacent_list[node].append([edge[1], eval(edge[2])])

#Dijkstra Algorithm Initialization
#set distance to a very large int 0xFFFFFFFF
dist_to_s = dict(zip(all_nodes, [0xFFFFFFFF]*len(all_nodes)))
nodes_queue = []
start_node = "1"
dist_to_s[start_node] = 0
nodes_queue += all_nodes

#Dijkstra: calculate the min distance of each node to the source node using Greedy Algorithm
while len(nodes_queue) > 0:

    v = min(nodes_queue, key = lambda x: dist_to_s[x])
    nodes_queue.remove(v)
    for node_dist in adjacent_list[v]:
        node = node_dist[0]
        dist = node_dist[1]

        temp_dist = dist_to_s[v] + dist
        if temp_dist < dist_to_s[node]:
            dist_to_s[node] = temp_dist

#print the distance of each node
for node in all_nodes:
    if dist_to_s[node] == 0xFFFFFFFF:
        print -1,
    else:
        print dist_to_s[node],