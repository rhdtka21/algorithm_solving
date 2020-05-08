# [파이썬 | BOJ | 10885] 공항
import sys
read = sys.stdin.readline

G = int(read())
P = int(read())
gi = []
info = {}

for _ in range(P):
    gi.append(int(read()))

def findGate(each_gate):
    temp = []
    while info.get(each_gate) is not None:
        each_gate = info[each_gate]
        temp.append(each_gate)
    for t in temp:
        info[t] = each_gate - 1
    info[each_gate] = each_gate - 1
    return each_gate

cnt = 0
for each_gate in gi:
    ans = findGate(each_gate)
    if ans == 0:
        break
    else:
        cnt += 1
print(cnt)