# [파이썬 | BOJ | 11401] 이항 계수 3

import sys
read = sys.stdin.readline

def power(a, b):
    ret = 1
    while b>0:
        if b % 2:       # b가 홀수이면
            ret *= a
            ret %= p
        a *= a
        a %= p
        b //= 2;
    return ret

p = 1000000007
N, K = map(int, read().split())

fact = [1 for _ in range(N+1)]

for i in range(2, N+1):
    fact[i] = fact[i-1] * i % p

A = fact[N]
B = (fact[N-K] * fact[K]) % p

# (A/B) % p 
# = A * B^-1 % p 
# = A * B^-1 * B^p-1 % p 
# = A * B^p-2 % p 
# = (A % p) * (B^p-2 % p) % p 
print((A % p) * (power(B, p-2) % p) % p )
