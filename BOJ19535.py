# [파이썬 | BOJ | 19535] ㄷㄷㄷㅈ
import sys
read = sys.stdin.readline


def comb(a, b):
    ans = 1
    if a-b < b:
        b = a-b
    for i in range(a-b+1, a+1):
        ans *= i
    for j in range(1, b+1):
        ans //=j
    return ans

N = int(read())
edge = []
degree = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, read().split())
    edge.append([a, b])
    degree[a] += 1
    degree[b] += 1

du = 0
ga = 0

for e in edge:
    temp = (degree[e[0]]-1) * (degree[e[1]]-1)
    du += temp

for idx in range(1, N+1):
    if degree[idx] >= 3:
        ga += comb(degree[idx], 3)

#print(du, ga)

if du > 3 * ga:
    print('D')
elif du < 3 * ga:
    print('G')
else:
    print('DUDUDUNGA')