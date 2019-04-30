class Trie:
    def __init__(self):
        self.counter = count(start=0)
        self.root = [next(self.counter), {}]
    
    def insert(self, sequence):
        node = self.root
        for base in sequence:
            if base not in node[1]:
                node[1][base] = [next(self.counter), {}] 
            node = node[1][base]
            
def trie(list_of_seqs):
    theTrie = Trie()
    for seq in list_of_seqs:
        theTrie.insert(seq)
    return theTrie.root


def Format(node):
    #print result
    for char, node2 in node[1].iteritems():
        result.append(str(node[0]) + '->' + str(node2[0]) + ':' + str(char))
        Format(node2)
    return result



if __name__ == '__main__':

    from itertools import count
    
    
    seqs=open("rosalind_ba9a.txt","r").read().rstrip().split("\n")
    
    result = []
    f = open('output.txt','w')
    for item in Format(trie(seqs)):
        f.write(item + '\n')
    f.close()