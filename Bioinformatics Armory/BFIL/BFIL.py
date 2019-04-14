from Bio import SeqIO
'''
return starting and ending indice of trimmed seq
'''
def trim_ind(quality_vec, threshold):
    for i in range(len(quality_vec)):
        if quality_vec[i] >= threshold:
            start_idx = i
            break
    for i in range(len(quality_vec))[::-1]:
        if quality_vec[i] >= threshold:
            end_idx = i
            break
    return [start_idx, end_idx]

'''
Calculate the quality scores and trimmed fastq reads cannot be done in the same iteration
VERY STUPID
'''

with open("rosalind_bfil.txt", 'r') as dataset:
    #read line by line, first line as average quality and the rest goes to SeqIO for parsing
    threshold = eval(dataset.readline())
    data = SeqIO.parse(dataset, 'fastq')
    trimmed_pos = []
    #get trimmed position for each fastq
    for record in data:
        quality_vec = [eval(x) for x in "\n".join(record.format('qual').rstrip().split("\n")[1:]).split()]
        trimmed_pos.append(trim_ind(quality_vec, threshold))
dataset.close()


output_content = open("rosalind_bfil.txt", 'r').read().rstrip().split("\n")

'''
Very stupid way of formating outputs, need improvement
'''

for k in range(len(output_content[1:])/4):
    [start_pos, end_pos] = trimmed_pos[k]
    print output_content[4*k+1]
    print output_content[4*k+2][start_pos : (end_pos+1)]
    print output_content[4*k+3]
    print output_content[4*k+4][start_pos : (end_pos+1)]