'''
read data
'''
data_file = open("rosalind_ba3h.txt","r").read().rstrip().split("\n")

k = eval(data_file[0])

list_of_kmers = data_file[1:]

'''
Initialize the result string with first kmer in the list
'''
result = list_of_kmers.pop(0)


'''
Identify kmer neighbors and paste to result
'''
while len(list_of_kmers) > 0:
    temp_list = list(list_of_kmers)
    
    for kmer in list_of_kmers:
        if kmer[:k-1] == result[-(k-1):]:
            result = result + kmer[k-1]
            temp_list.remove(kmer)
        elif kmer[-(k-1):] == result[:k-1]:
            result = kmer[0] + result
            temp_list.remove(kmer)
    
    list_of_kmers = list(temp_list)
        
        
print result          