'''
Function of distance calculation for trees in Newick format

Basic ideas by Eugene Baulin:

Algorithm idea
left = the start location of the node in the left

right = the start location of the node in the right

go from left to right:

distance = number of mismatching right backets + number of mismatching left backets 
            + 2*(whether there is a comma after the last mismatching right backet).
'''

def distance_calculator(fragment):
    
    dist = 0
    
    #handle cases where both nodes are sharing the same parent node (A,,,,,B) case
    if fragment.count(')') == 0:
        return (dist+2)
    
    #handle regular cases where node A and node B have different parents
    #push everything into a stack get num of mismatched left and right brackets
    stack = ''
    for i in range(len(fragment)):
        if fragment[i] == ')' or fragment[i] == '(':
            if len(stack) >0 and stack[0] == '(' and fragment[i] == ')':
                stack = stack[1:]
            else:
                stack = fragment[i] + stack
        
    dist = stack.count('(') + stack.count(')')
    
    #check if there is a comma after the last mismatched right bracket
    for j in range(len(fragment)-1)[::-1]:
        if fragment[j]==')':
            if fragment[j+1] == ',':
                return dist + 2
            else:
                return dist
                
    
    
    return(dist)

if __name__ == '__main__':

    #read and process data    
    data_files = open("rosalind_nwck.txt", 'r').read().split()
    list_of_all_pairs = zip(data_files[1::3], data_files[2::3])
    list_of_graphs = data_files[0::3]

    #select the region between two nodes 
    list_of_regions_in_between = []

    for i in range(len(list_of_graphs)):
        seq = list_of_graphs[i]
        start_idx = seq.index(list_of_all_pairs[i][0])
        end_idx =  seq.index(list_of_all_pairs[i][1])
    
        if end_idx > start_idx:
            list_of_regions_in_between.append(seq[start_idx + len(list_of_all_pairs[i][0]):end_idx])
        else:
            list_of_regions_in_between.append(seq[end_idx + len(list_of_all_pairs[i][1]):start_idx])




    #calculate distance and output the result
    print(' '.join(str(distance_calculator(fragment)) for fragment in list_of_regions_in_between))