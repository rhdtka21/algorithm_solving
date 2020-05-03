# [파이썬 | BOJ | 16637] 괄호 추가하기

import sys
from collections import deque
from copy import deepcopy
read = sys.stdin.readline
maxAns = sys.maxsize * -1

def myCal(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '!':
        return num1


def case(check, depth):
    if depth == opNum:
        solve(check)
        return

    if depth > 0 and check[depth-1] == 1:
        check[depth] = 0
        case(check, depth+1)
    else:
        check[depth] = 0
        case(check, depth+1)
        check[depth] = 1
        case(check, depth+1)

def solve(check):
    global maxAns

    nums = deepcopy(originNums)
    ops = deepcopy(originOps)

    for i, c in enumerate(check):
        if c == 1:
            retVal = myCal(nums[i], ops[i], nums[i+1])
            nums[i] = retVal
            ops[i] = '!'
    #print(nums, ops)
    while ops:
        retVal = myCal(nums[0], ops[0], nums[1])
        nums.pop(1)
        nums[0] = retVal
        ops.pop(0)

    ans = nums[0]
    if ans > maxAns:
        maxAns = ans
    return


N = int(read())
calstr = read().replace('\n', '')
originNums = []
originOps = []
for i in range(N):
    if i%2 == 0:
        originNums.append(int(calstr[i]))
    else:
        originOps.append(calstr[i])

opNum = len(originOps)
case([0 for _ in range(opNum)], 0)
print(maxAns)