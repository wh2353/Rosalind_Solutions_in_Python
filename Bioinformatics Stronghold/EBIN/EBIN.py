data_file = open("rosalind_ebin.txt","r").read().rstrip().split("\n")
print ' '.join(map(lambda x: str(eval(data_file[0])*x), (eval(x) for x in data_file[1].split())))