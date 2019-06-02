'''
Implement the Max heap,
following the pseudocode available at:
https://en.wikipedia.org/wiki/Binary_heap
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
    
    
       


if __name__ == "__main__":
    data_file = open("rosalind_hea.txt","r").read().rstrip().split("\n")
    n = eval(data_file[0])
    A = [eval(x) for x in data_file[1].split()]
    
    for i in range((n/2))[::-1]:
        Max_Heapify(A, i)
    print " ".join(str(x) for x in A)
    f = open('output.txt', 'w')
    f.write(' '.join(str(x) for x in A))
    f.close()