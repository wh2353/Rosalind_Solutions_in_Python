from collections import defaultdict

'''
return reverse complement seq
'''
def reverse_complement(kmer):
    return kmer.replace('A', 't').replace('C', 'g').replace('G', 'c').replace('T', 'a').upper()[::-1]

'''
read file
'''
data_file = open("rosalind_ba6e.txt","r").read().rstrip().split("\n")
k = eval(data_file[0])
seq1, seq2 = data_file[1:]

dict_seq1 = defaultdict(list)

'''
Build a dictionary in which keys are kmers and values 
are list of start indices of that specific kmer
'''
for i in range(len(seq1)-k+1):
    dict_seq1[seq1[i:i+k]].append(i)
    

'''
write to output file
'''    
f = open("output.txt", "w")    
for j in range(len(seq2)-k+1):
    
    '''
    if a kmer of seq2 does not exist in seq1,
    an empty list will be returned, and 
    nothing print out to the file/console
    '''
    for i in dict_seq1[seq2[j:j+k]] + dict_seq1[reverse_complement(seq2[j:j+k])]:
        print str((i, j))
        f.write(str((i, j)) + '\n')

f.close()