from Bio import SeqIO
with open("rosalind_phre.txt", 'r') as dataset:
    #read line by line, first line as average quality and the rest goes to SeqIO for parsing
    average_quality = eval(dataset.readline())
    data = SeqIO.parse(dataset, 'fastq')
    #check sequence one by one
    count = 0
    for record in data: 
        final_list = [eval(x) for x in "\n".join(record.format('qual').rstrip().split("\n")[1:]).split()]
        if sum(final_list) / float(len(final_list)) < average_quality:
            count += 1
    print count
dataset.close()