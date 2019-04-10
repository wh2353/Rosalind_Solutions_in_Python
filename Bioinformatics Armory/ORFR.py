from Bio.Seq import translate

DNA_seq=open("rosalind_orfr.txt","r").read().rstrip()

rc_seq = DNA_seq.replace("A", 't').replace("C", 'g').replace("G", 'c').replace("T", 'a')[::-1].upper()


forward_orf_ind =[i for i in range(len(DNA_seq)-3+1) if DNA_seq[i:i+3] == 'ATG']

reverse_orf_ind =[i for i in range(len(rc_seq)-3+1) if rc_seq[i:i+3] == 'ATG']


list_of_AASeq = []

for idx in forward_orf_ind:
    list_of_AASeq.append(translate(DNA_seq[idx:], to_stop=True))
for idx in reverse_orf_ind:
    list_of_AASeq.append(translate(rc_seq[idx:], to_stop=True))



print max(list_of_AASeq, key=len)