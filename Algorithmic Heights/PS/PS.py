data_file = open("rosalind_ps.txt","r").read().rstrip().split("\n")
n = eval(data_file[0])
A = sorted([eval(x) for x in data_file[1].split()])
k = eval(data_file[2])

print ' '.join(str(x) for x in A[:k])