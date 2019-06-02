import time
'''
Implement HeapSort
Very slow, need to shift to inplace sort
to increase efficiency
'''
def Max_Heapify(A, i):
    
    #add 1 to both left and right children as python indice start at zero rather than one
    left = 2*i+1
    right = 2*i+2
    largest = i
    
    if len(A) > max(left, right) and A[largest] < max(A[left], A[right]):
        
        if A[left] > A[largest]:
            largest = left
        if A[right] > A[largest]:
            largest = right

    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Max_Heapify(A, largest)
    
def Max_Heap_builder(A):
    for i in range((len(A)/2))[::-1]:
        Max_Heapify(A, i)
        

    
        
if __name__ == "__main__":
    start = time.time()
    data_file = open("rosalind_hs.txt","r").read().rstrip().split("\n")
    n = eval(data_file[0])
    A = [eval(x) for x in data_file[1].split()]
    Max_Heap_builder(A)
    sorted_seq = []

    while len(A)>0:
        
        sorted_seq = [A[0]] + sorted_seq
        A[0], A[-1] = A[-1], A[0]
        A = A[:-1]
        Max_Heapify(A, 0)
    
        #print A
    print ' '.join(str(x) for x in sorted_seq)
    f = open('output.txt', 'w')
    f.write(' '.join(str(x) for x in sorted_seq))
    f.close()
    print "finished"
    end = time.time()
    print "total running time: " + str(end - start) + "seconds"