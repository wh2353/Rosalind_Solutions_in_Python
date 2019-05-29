'''
Implement the quicksort algorithm,
following the pseudocode available at:
https://en.wikipedia.org/wiki/Quicksort
'''
def partition(lo, hi):
    pivot = A[hi-1]
    i = lo
    for j in range(lo, hi-1):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[hi-1] = A[hi-1], A[i]
    return i

def quick_sort(lo, hi):
    if lo < hi-1:
        p = partition(lo, hi)
        quick_sort(lo, p)
        quick_sort(p+1, hi)
    return A

if __name__ == "__main__":
    data_file = open("rosalind_qs.txt","r").read().rstrip().split("\n")
    n = eval(data_file[0])
    A = [eval(x) for x in data_file[1].split()]
    #print ' '.join(str(x) for x in quick_sort(0, n))
    f = open('output.txt', 'w')
    f.write(' '.join(str(x) for x in quick_sort(0, n)))
    f.close()

