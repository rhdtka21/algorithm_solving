# [파이썬 | BOJ | 2661] 좋은 수열

import sys
read = sys.stdin.readline

def isok(string):
    
    length = len(string)
    tempLength = range(2,length+1,2)
    string = ''.join(reversed(string))
    for temp in tempLength:
        if string[:temp//2] == string[temp//2:temp//2 * 2]:
            return False
    return True

def solve(index, ans):
    if index == N:
        print(ans)
        sys.exit(0)
        return
    
    for i in ('1', '2', '3'):
        if isok(ans+i):
            solve(index+1, ans+i)


N = int(read())
solve(1, '1')