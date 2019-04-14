import numpy as np
from Bio import SeqIO
with open("rosalind_bphr.txt", 'r') as dataset:
    #read line by line, first line as average quality and the rest goes to SeqIO for parsing
    threshold = eval(dataset.readline())
    data = SeqIO.parse(dataset, 'fastq')

    #get overall quality of each base position
    overall_qual = np.array([[eval(x) for x in "\n"\
    	.join(record.format('qual').rstrip().split("\n")[1:]).split()] for record in data]).T 
    #output the number of low quality base positions
    print sum(sum(pos_qual)/float(len(pos_qual)) < threshold for pos_qual in overall_qual)

dataset.close()