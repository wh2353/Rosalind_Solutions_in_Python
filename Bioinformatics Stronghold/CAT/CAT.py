memo = {}
memo[""] = 1
def is_complement(base1, base2):
    if 'AU' in base1+base2 or 'UA' in base1+base2 :
        return True
    elif 'GC' in base1+base2 or 'CG' in base1+base2 :
        return True

    return False

def find_noncrossmatch(S):
    if S in memo.keys():
        return memo[S]
    elif S.count('A')!=S.count('U') or S.count('G')!=S.count('C'):
        return 0
    result = 0
    #search all possible complement based with S[0] as potential divide lines
    for i in range(1,len(S)):
        if is_complement(S[0], S[i]):
            result += find_noncrossmatch(S[1:i])*find_noncrossmatch(S[i+1:])
    memo[S] = result
    return result

seq = "".join(open("rosalind_cat.txt", "r").read().rstrip().split("\n")[1:])

print find_noncrossmatch(seq) % 10**6