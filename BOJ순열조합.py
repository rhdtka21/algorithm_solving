import sys
read = sys.stdin.readline
temp = []

def perm_recur():
    if len(temp) == M:
        print(temp)
        return
    for i in range(N):
        if not check[i]:
            check[i] = 1
            temp.append(i)
            perm_recur()
            temp.pop()
            check[i] = 0

def comb_recur(idx, chosen):
    if(idx == N):
        if(len(chosen) == M):
            yield chosen
    check[idx] = 1           #골랐다.
    comb_recur(idx+1, chosen + [idx+1])
    check[idx] = 0
    comb_recur(idx+1, chosen)

def combinations(arr,r):
    for i in range(len(arr)):  
        if r == 1:  
            yield [arr[i]]
        else:
            for c in combinations(arr[i+1:],r-1):
                yield [arr[i]] + c

def combinations_repetition(arr,r):
    for i in range(len(arr)):  
        if r == 1:  
            yield [arr[i]]
        else:
            for c in combinations_repetition(arr[i:],r-1):
                yield [arr[i]] + c

def permutation_repetition(arr,r):
    for i in range(len(arr)):  
        if r == 1:  
            yield [arr[i]]
        else:
            for c in permutation_repetition(arr, r-1):
                yield [arr[i]] + c

N, M = map(int, read().split())
arr = sorted(list(map(int, read().split())))
check = [0 for _ in range(N)]

for c in combinations_repetition(range(N), M):
    for idx in c:
        print(arr[idx], end=' ')
    print()
