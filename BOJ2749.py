# [파이썬 | BOJ | 2749] 피보나치 수 3
 
import sys
read = sys.stdin.readline
p = 1000000

def dot(mat1, mat2):
    N = len(mat1)
    M = len(mat2)
    K = len(mat1[0])
    ansmat = [[0 for _ in range(K)] for _ in range(N)]
    for i in range(N):
        for j in range(K):
            temp = 0
            for k in range(M):
                temp += mat1[i][k] * mat2[k][j] % p
            ansmat[i][j] = temp % p
    return ansmat

def power(mat, b):
    # 행렬의 제곱은 무조건 N * N꼴이다.
    N = len(mat)
    ret = [[0 for _ in range(N)] for _ in range(N)]
    # ret = 단위행렬
    for i in range(N):
        ret[i][i] = 1

    while b>0 :
        if b%2 :
            ret = dot(mat, ret)
        mat = dot(mat, mat)
        b //= 2
    return ret

N = int(read())
mat = [[1, 1], [1, 0]]
if N == 1:
    print(1)
else:
    fibmat = power(mat, N-1)
    ans = fibmat[0][0]
    print(ans)
