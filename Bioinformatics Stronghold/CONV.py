import collections
list_of_sets=open("rosalind_conv.txt","r").read().rstrip().split("\n")
set1 = map(lambda x: eval(x), list_of_sets[0].split())
set2 = map(lambda x: eval(x), list_of_sets[1].split())

most_freq_counts_with_key = collections.Counter([round(val1 - val2, 5) for val1 in set1 for val2 in set2]).most_common(1)

print "\n".join(map(lambda x: str(x), most_freq_counts_with_key[0][::-1]))