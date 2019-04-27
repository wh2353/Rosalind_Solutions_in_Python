'''
Check whether two RNA bases are complementary to each other
'''
def is_complement(base1, base2):
    return base1+base2 == 'AU' or base1+base2 == 'UA' or\
           base1+base2 == 'CG' or base1+base2 == 'GC'
    
'''
Recursive algorithm to calculate Motzkin number
with taking into consideration that edges can only happen
between complementary basepairs
'''    

def Motzkin_number(seq):
    if len(seq) <= 1:
        return 1
    elif seq in Motzkin_number_library:
        return Motzkin_number_library[seq]
    else:
        Motzkin_number_library[seq] = Motzkin_number(seq[1:])
        
        for i in range(1, len(seq)):
            if is_complement(seq[i], seq[0]):
                Motzkin_number_library[seq] += Motzkin_number(seq[1:i])*Motzkin_number(seq[i+1:]) 
    
    return Motzkin_number_library[seq]
        

'''
read input, initialize Motzkin number library,
run the algorithm and output the final result
'''
RNA_seq = ''.join(open("rosalind_motz.txt","r").read().rstrip().split("\n")[1:])
Motzkin_number_library = {}

print Motzkin_number(RNA_seq) % 1000000