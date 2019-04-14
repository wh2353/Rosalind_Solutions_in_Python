from Bio import SeqIO
with open("rosalind_filt.txt", 'r') as dataset:
    #read line by line, first line as average quality and the rest goes to SeqIO for parsing
    threshold_and_percent = dataset.readline()
    threshold = eval(threshold_and_percent.split()[0])
    percent = eval(threshold_and_percent.split()[1])
    data = SeqIO.parse(dataset, 'fastq')
    count = 0
    for record in data:
        quality_vec = [eval(x) for x in "\n".join(record.format('qual').rstrip().split("\n")[1:]).split()]
        #count all good reads
        if (sum(int(x >= threshold) for x in quality_vec) / float(len(quality_vec)))*100 >= percent:
            count += 1
        
    print count
    
dataset.close()